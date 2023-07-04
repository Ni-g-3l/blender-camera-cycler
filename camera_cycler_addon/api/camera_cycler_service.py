from camera_cycler_addon.domain.scene_camera_manager import SceneCameraManager

class CameraCyclerService(object):

    @classmethod
    def get_next_camera(cls, camera_list, current_camera):
        return SceneCameraManager.get_next_camera(camera_list, current_camera)

    @classmethod
    def get_previous_camera(cls, camera_list, current_camera):
        return SceneCameraManager.get_previous_camera(camera_list, current_camera)