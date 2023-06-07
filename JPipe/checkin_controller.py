import importlib
from JPipe.settings import SettingsResolver

class CheckinController:
    """Base class for all the check in processes."""
    
    def __init__(self, settings_file: str, application: str):
        """Instantiate all the necessary objects given the provided settings."""
        self.settings = SettingsResolver(settings_file)
        self.application = application

        self.application_controller = self.settings.application_handler
        self.disk_handler = self.settings.disk_handler

    def checkin(self):
        """Perform the check in process."""
        raise NotImplementedError("CheckinController.checkin() not implemented.")
    
    def validate(self) -> tuple[list, list]:
        """Get all the validations from the provided settings and run them."""
        raise NotImplementedError("Validation is not implemented.")
        
                