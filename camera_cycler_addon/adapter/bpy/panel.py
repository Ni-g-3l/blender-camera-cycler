import bpy

from camera_cycler_addon.adapter.bpy.operator import SelectNextCameraOperator, SelectPreviousCameraOperator, ToggleCameraViewOperator
    
class CameraCyclerPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_camera_cycler_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_label = "Camera"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(ToggleCameraViewOperator.bl_idname, text="Active Camera", icon="OUTLINER_OB_CAMERA")

        split = layout.split(align=True)
        
        col = split.column()
        col.operator(SelectPreviousCameraOperator.bl_idname, text="Previous", icon="TRIA_LEFT_BAR")

        col = split.column()
        col.operator(SelectNextCameraOperator.bl_idname, text="Next", icon="TRIA_RIGHT_BAR")