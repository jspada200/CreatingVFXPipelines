from ..validator_base import ValidatorBase

class ValidateReferences(ValidatorBase):
    """
    Validate that all links in the application are valid.
    """
    display_name = "References"

    def validate(self):
        """
        Validate that all the files reference in the currently open scene are valid.
        :return:
        """
        all_refrenced_files = self.application_provider.get_all_referenced_files()
        files_that_do_not_exist = []
        for file in all_refrenced_files:
            if not self.disk_provider.file_exists(file):
                files_that_do_not_exist.append(file)
        if files_that_do_not_exist:
            return False, f"The following files do not exist: {files_that_do_not_exist}"
        return True, None
