from JPipe.checkin_controller import CheckinController


class CommandLineCheckin(CheckinController):
    def __init__(self,
                 settings_file: str,
                 application: str,
                 scene_file_path: str,
                 force=False):
        super().__init__(settings_file,application)
        self.force = force
        self.scene_file_path = scene_file_path


    def checkin(self):
        """
        Run the entire check in process in a single call.

        This includes and hooks or validations that need to occur.
        :return:
        """
        self.application_controller.open_scene(self.scene_file_path)
        success, failed = self.validate()

        if not self.force and failed:
            print(f"Validation failed. Not checking in.")
            return False

new_control = CommandLineCheckin(r"C:\Users\tex18\PycharmProjects\CreatingVFXPipelines\JPipe\example_settings.json", "maya", "C:/Users/tyler/Desktop/test.ma")