import importlib
from JPipe.settings import SettingsResolver
from JPipe.base import JPipeBase

class CheckinController(JPipeBase):
    """Base class for all the check in processes."""
    
    def __init__(self, settings_file: str, application: str):
        """Instantiate all the necessary objects given the provided settings."""
        super().__init__()
        self.settings = SettingsResolver(settings_file, application)
        self.application = application

        self.application_provider = self.settings.application_provider
        self.disk_provider = self.settings.disk_provider

        self.checkin_files = []

    def checkin(self):
        """Perform the check in process."""
        raise NotImplementedError("CheckinController.checkin() not implemented.")
    
    def validate(self) -> tuple[list, list]:
        """Get all the validations from the provided settings and run them."""
        raise NotImplementedError("Validation is not implemented.")
        
                