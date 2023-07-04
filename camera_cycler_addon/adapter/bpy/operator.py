import bpy

from camera_cycler_addon.api.camera_cycler_service import CameraCyclerService

class CameraOperator:

    @classmethod
    def list_cameras(cls):
        return [ob for ob in bpy.context.scene.objects if ob.type == 'CAMERA']

class SelectNextCameraOperator(bpy.types.Operator, CameraOperator):

    bl_idname = "camera.select_next_camera"
    bl_label = "Next Camera"

    def execute(self, context):
        camera_list = self.list_cameras()
        new_camera = CameraCyclerService.get_next_camera(camera_list, context.scene.camera)
        new_camera.select_set(True)
        context.scene.camera = new_camera
        return {"FINISHED"}

class SelectPreviousCameraOperator(bpy.types.Operator, CameraOperator):

    bl_idname = "camera.select_previous_camera"
    bl_label = "Previous Camera"

    def execute(self, context):
        camera_list = self.list_cameras()
        new_camera = CameraCyclerService.get_previous_camera(camera_list, context.scene.camera)
        new_camera.select_set(True)
        context.scene.camera = new_camera
        return {"FINISHED"}

class ToggleCameraViewOperator(bpy.types.Operator):

    bl_idname = "camera.toggle_view"
    bl_label = "Toggle Camera"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                if area.spaces[0].region_3d.view_perspective == 'CAMERA':
                    area.spaces[0].region_3d.view_perspective = 'PERSP'
                else:
                    area.spaces[0].region_3d.view_perspective = 'CAMERA'
        return {"FINISHED"}