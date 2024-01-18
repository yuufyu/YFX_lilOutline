from typing import ClassVar

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


def bake_normal_average(obj: bpy.types.Object, shrink_tip_strength: float) -> None:
    eps = 0.000001

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

            if shrink_tip_strength > eps:
                dot_product = max(
                    0.0,
                    min(1.0, mathutils.Vector.dot(normal, normal_average)),
                )
                width = dot_product**shrink_tip_strength
            else:
                # To avoid overwriting the existing vertex color alpha value
                width = vcol_layer.data[loop_index].color[3]

            vcol_layer.data[loop_index].color = (
                mathutils.Vector.dot(normal_average, tangent) * 0.5 + 0.5,
                mathutils.Vector.dot(normal_average, bitangent) * 0.5 + 0.5,
                mathutils.Vector.dot(normal_average, normal) * 0.5 + 0.5,
                width,
            )


class YFX_LILOUTLINE_OT_smooth_outlines(bpy.types.Operator):
    bl_idname = "yfx_liloutline.smooth_outlines"
    bl_label = "Smooth Outlines"
    bl_description = "Smooth the outline direction by baking in vertex colors"
    bl_options: ClassVar[set] = {"REGISTER", "UNDO"}

    shrink_tip_strength: bpy.props.FloatProperty(
        name="Shrink Tip Strength",
        description="The strength of converging the tip portion of the outline",
        default=0.0,
        min=0.0,
    )

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
                bake_normal_average(obj, self.shrink_tip_strength)
        return {"FINISHED"}
