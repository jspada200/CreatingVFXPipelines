import os.path

from JPipe.checkin_controller import CheckinController

class CommandLineCheckin(CheckinController):
    def __init__(self,
                 settings_file: str,
                 application: str,
                 scene_file_path: str,
                 entity_type: str,
                 entity_name: str,
                 project_directory: str,
                 force=False):
        super().__init__(settings_file,application)
        self.force = force
        self.scene_file_path = scene_file_path
        self.entity_type = entity_type
        self.entity_name = entity_name
        self.project_directory = project_directory


    def checkin(self):
        """
        Run the entire check in process in a single call.

        This includes and hooks or validations that need to occur.
        :return:
        """
        self.info(f"Starting checkin of {os.path.basename(self.scene_file_path)}...")

        try:
            self.application_provider.open_scene(self.scene_file_path)
        except Exception as e:
            self.error(f"Failed to open scene {os.path.basename(self.scene_file_path)}.")
            self.error(str(e))
            return False

        print("Starting Validation...")
        success, failed = self.validate()

        if not self.force and failed:
            self.error(f"Validation failed. Not checking in.")
            return False
        elif failed:
            self.warn(f"Validation failed, but force flag is set. Checking in anyway.")
        else:
            self.info(f"Validation passed. Checking in.")

        self.info(f"Running hooks...")
        for hook in self.settings.get_hooks():
            hook(self).run()

        self.info(f"Checkin of {os.path.basename(self.scene_file_path)} complete.")
        self.info(f"Checkin files:")
        for file in self.checkin_files:
            self.info(file)

    def validate(self) -> tuple[list, list]:
        """
        Validate the provided scene file. At this point the scene should be open.
        :return: List of Successful and failed Validations.
        """
        success, failed = [], []
        for validation in self.settings.get_validators():
            result, message = validation.validate()
            if result:
                success.append(validation)
                self.info(f"{validation.display_name} Validation passed.")
            else:
                failed.append(validation)
                self.error(f"{validation.display_name} Validation failed: {message}")

        return success, failed

    def execute_checkin(self):
        """
        Execute the checkin process that will create the needed locations and publish the files.
        :return:
        """
        pass