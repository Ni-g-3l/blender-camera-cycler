bl_info = {
    "name": "{{cookiecutter.blender_addon_name}}",
    "author": "{{cookiecutter.author}}",
    "version": (0, 1),
    "blender": (3, 5, 1),
    "location": "{{cookiecutter.blender_addon_location}}",
    "description": "{{cookiecutter.blender_addon_description}}",
    "warning": "",
    "doc_url": "https://github.com/{{cookiecutter.author}}/{{cookiecutter.blender_addon_git_name}}",
    "category": "{{cookiecutter.blender_addon_category}}",
}

from camera_cycler_addon import bpy_loader

def register():
    bpy_loader.register()

def unregister():
    bpy_loader.unregister()

