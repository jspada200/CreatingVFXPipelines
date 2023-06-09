import os.path

from JPipe.checkin_controller import CheckinController
from colorama import init
from colorama import Fore, Back, Style
init()

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
        print(f"Starting checkin of {os.path.basename(self.scene_file_path)}...")

        try:
            self.application_controller.open_scene(self.scene_file_path)
        except Exception as e:
            print(Fore.RED + f"Failed to open scene {os.path.basename(self.scene_file_path)}.")
            print(Fore.LIGHTRED_EX + str(e))
            return False

        print("Starting Validation...")
        success, failed = self.validate()

        if not self.force and failed:
            print(Fore.RED + f"Validation failed. Not checking in.")
            return False
        elif failed:
            print(Fore.YELLOW + f"Validation failed, but force flag is set. Checking in anyway.")
        else:
            print(Fore.GREEN + f"Validation passed. Checking in.")

    def validate(self) -> tuple[list, list]:
        """
        Validate the provided scene file. At this point the scene should be open.
        :return: List of Successful and failed Validations.
        """
        success, failed = [], []
        print(Style.RESET_ALL)
        for validation in self.settings.get_validators():
            result, message = validation.validate()
            if result:
                success.append(validation)
                print(Fore.LIGHTGREEN_EX +f"{validation.display_name} Validation passed.")
            else:
                failed.append(validation)
                print(Fore.RED + f"{validation.display_name} Validation failed: {message}")
        print(Style.RESET_ALL)
        return success, failed
