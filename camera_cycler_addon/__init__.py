bl_info = {
    "name": "Camera Cycler",
    "author": "Ni-g-3l",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "3D View",
    "description": "Navigate throught all scene camera.",
    "warning": "",
    "doc_url": "https://github.com/Ni-g-3l/blender-camera-cycler",
    "category": "Camera",
}

from camera_cycler_addon import bpy_loader

def register():
    bpy_loader.register()

def unregister():
    bpy_loader.unregister()

