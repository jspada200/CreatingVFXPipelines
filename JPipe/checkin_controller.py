import importlib

class CheckinController:
    """Base class for all the check in processes."""
    
    def __init__(self, settings: dict):
        """Instantiate all the necessary objects given the provided settings."""
        self.settings = settings
        
        self.disk_handler = self.import_object_from_string(settings["disk_handler"])
        
        self.application_controller = self.import_object_from_string(
            settings["application_controller"])
        
        
    def import_object_from_string(self, object_string: str):
        """Import an object from a string."""
        
        module_name, class_name = object_string.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    
    def checkin(self):
        """Perform the check in process."""
        raise NotImplementedError("CheckinController.checkin() not implemented.")
    
    def validate(self):
        """Get all the validations from the provided settings and run them."""
        failed_validations = []
        successful_validations = []
        for validation in self.settings["validations"]:
            cls = self.import_object_from_string(validation)
            validation_obj = cls(self.application_controller, self.disk_handler)
            
            status, msg = validation_obj.validate()
            
            if status:
                successful_validations.append(validation)
            else:
                failed_validations.append(msg)
        
                