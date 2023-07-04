class SceneCameraManager(object):

    @classmethod
    def get_next_camera(cls, camera_list, current_camera):
        camera_index = camera_list.index(current_camera)
        
        if camera_index == len(camera_list) - 1:
            return camera_list[0]

        return camera_list[camera_index + 1]
    
    @classmethod
    def get_previous_camera(cls, camera_list, current_camera):
        camera_index = camera_list.index(current_camera)
        return camera_list[camera_index - 1]
