# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "HiFi Blender Add-on",
    "author": "Matti 'Menithal' Lahtinen",
    "version": (0,0,1),
    "blender": (2,7,7),
    "location": "File > Import-Export, Materials, Armature",
    "description": "Blender tools to allow for easier Content creation for High Fidelity",
    "warning": "",
    "wiki_url": "",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

import addon_utils
import importlib
import sys
import bpy

from hifi_json_loader import *


if "add_mesh_extra_objects" not in addon_utils.addons_fake_modules:
    print(" Could not find add_mesh_extra_objects, Trying to add it automatically. Otherwise install it first via Blender Add Ons")
    addon_utils.enable("add_mesh_extra_objects")
    
def reload_module(name): 
    if name in sys.modules: 
        del sys.modules[name]

reload_module('hifi_scene')
reload_module('bpy_util')   
reload_module('hifi_primitives')  
reload_module('hifi_json_loader')    
    

    
def menu_func_import(self, context):
    self.layout.operator(HifiJsonOperator.bl_idname, text="High Fidelity JSON (.json)")
    
    
def register():
    bpy.utils.register_class(HifiJsonOperator)
    bpy.types.INFO_MT_file_import.append(menu_func_import)
 
def unregister():
    bpy.utils.unregister_class(HifiJsonOperator)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)

 
if __name__ == "__main__":
    register()