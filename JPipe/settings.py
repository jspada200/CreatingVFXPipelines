from JPipe import base
import json


def _get_class(class_path: str):
    """Returns a class from a string path."""
    module_path, class_name = class_path.rsplit('.', 1)
    module = __import__(module_path, fromlist=[class_name])
    return getattr(module, class_name)


class SettingsResolver(base.JPipeBase):
    """
    Resolves settings and imports libraries that are needed.
    """

    def __init__(self, settings_file_path: str, application: str):
        super().__init__()
        self._application = application
        self._settings_file_path = settings_file_path
        with open(self._settings_file_path, 'r') as f:
            self._settings = json.load(f)

        self._application_handler = None
        self._disk_handler = None

    def validate(self):
        """Ensure we have the correct keys set on the settings obj."""
        required_keys = [
            'application_handler',
            'disk_handler',
            'validators',
            'hooks',]

        for key in required_keys:
            if key not in self._settings:
                raise KeyError(f"Settings file missing required key: {key}")

    @property
    def application_handler(self):
        """Returns the application handler class."""
        if not self._application_handler:
            self._application_handler = \
                _get_class(self._settings['application_handler'][self._application])()
        return self._application_handler

    @property
    def disk_handler(self):
        """Returns the disk handler class."""
        if not self._disk_handler:
            self._disk_handler = _get_class(self._settings['disk_handler'])()
        return self._disk_handler

    def get_validators(self):
        """
        Returns a list of validator classes.
        :param application: The application to get the validators for.
        :returns list: A list of validator classes.
        """
        validators = []
        for validator in self._settings['validators'].get(self._application, []):
            validators.append(_get_class(validator)(self.application_handler, self.disk_handler))
        return validators

    def get_hooks(self):
        """
        Returns a list of hook classes.
        :param application: The application to get the validators for.
        :returns list: A list of validator classes.
        """
        hooks = []
        for hook in self._settings['hooks'].get(self._application, []):
            hooks.append(_get_class(hook))
        return hooks