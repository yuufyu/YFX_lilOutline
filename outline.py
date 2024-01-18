import bpy
import mathutils


def get_vertex_normals(mesh: bpy.types.Mesh) -> list:
    normals = [v.normal for v in mesh.vertices]
    if mesh.has_custom_normals:
        for poly in mesh.polygons:
            for loop_index in poly.loop_indices:
                mesh_loop = mesh.loops[loop_index]
                normals[mesh_loop.vertex_index] = mesh_loop.normal

    return normals


def bake_normal_average(obj: bpy.types.Object) -> None:
    mesh = obj.data
    mesh.calc_tangents()

    # Get Vertex Normals
    normals = get_vertex_normals(mesh)

    # Setup VertexColors
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()

    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            vertex = mesh.loops[loop_index]
            tangent = vertex.tangent
            bitangent = vertex.bitangent
            normal = vertex.normal
            normal_average = normals[vertex.vertex_index]

            vcol_layer.data[loop_index].color = (
                mathutils.Vector.dot(normal_average, tangent) * 0.5 + 0.5,
                mathutils.Vector.dot(normal_average, bitangent) * 0.5 + 0.5,
                mathutils.Vector.dot(normal_average, normal) * 0.5 + 0.5,
                1.0,
            )


class YFX_LILOUTLINE_OT_smooth_outlines(bpy.types.Operator):
    bl_idname = "yfx_liloutline.smooth_outlines"
    bl_label = "Smooth Outlines"
    bl_description = "Smooth the outline direction by baking in vertex colors"

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return (
            context.mode == "OBJECT"
            and context.active_object
            and context.active_object.type == "MESH"
        )

    def execute(self, context: bpy.types.Context) -> set:
        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                bake_normal_average(obj)
        return {"FINISHED"}
