# ##### BEGIN GPL LICENSE BLOCK #####
# Copyright (C) 2024 yuufyu
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

from .outline import YFX_LILOUTLINE_OT_smooth_outlines  # Import the operator module

bl_info = {
    "name": "YFX lilOutline",
    "description": "This Blender add-on enhances the appearance of outlines rendered using the 'lilToon'(https://github.com/lilxyzw/lilToon) shader by providing a smoother look.\
It achieves this by writing the direction of the outline into the vertex colors of the mesh.\
The lilToon shader utilizes the information stored in the vertex colors to control the direction of the outline.\
To leverage this feature, ensure that the lilToon shader's 'Outline > Vertex Color' setting is configured to 'RGBA -> Normal & Width'.\
This Blender add-on aims to bring functionality similar to 'lilOutlineUtil'(https://github.com/lilxyzw/lilOutlineUtil) in Unity to Blender.",
    "author": "yuufyu",
    "blender": (4, 0, 2),
    "version": (0, 0, 1),
    "category": "Object",
    "location": "View3D > Object > Smooth Outlines",
}


def menu_func(self: bpy.types.AnyType, context: bpy.types.Context) -> None:
    self.layout.operator(YFX_LILOUTLINE_OT_smooth_outlines.bl_idname)


classes = [
    YFX_LILOUTLINE_OT_smooth_outlines,
]


def register() -> None:
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister() -> None:
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
