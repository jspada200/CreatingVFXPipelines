import json
import unittest
from unittest import mock

import pytest

from ..settings import SettingsResolver
from ..application_handler import ApplicationHandler
from ..disk_handler import DiskHandler
from ..validator_base import ValidatorBase

class SettingsResolverTestCase(unittest.TestCase):
    def setUp(self):
        self.settings_file_path = "path/to/settings.json"
        self.settings = {
            "application_handler": "JPipe.application_handler.ApplicationHandler",
            "disk_handler": "JPipe.disk_handler.DiskHandler",
            "validators": {
                "my_app": [
                    "JPipe.validator_base.ValidatorBase",
                ]
            },
            "hooks": {
                "my_app": [
                    "JPipe.validator_base.ValidatorBase",
                ]
            },
        }
        with mock.patch(
            "builtins.open", mock.mock_open(read_data=json.dumps(self.settings))
        ) as mock_file:
            self.resolver = SettingsResolver(self.settings_file_path)

    def test_init_loads_settings_from_file(self):
        with mock.patch("builtins.open", mock.mock_open(read_data="{}")) as mock_file:
            resolver = SettingsResolver(self.settings_file_path)
            mock_file.assert_called_once_with(self.settings_file_path, "r")

    def test_validate_with_valid_settings(self):
        self.resolver._settings = self.settings
        self.resolver.validate()  # Should not raise an exception

    def test_validate_with_missing_key(self):
        invalid_settings = self.settings.copy()
        del invalid_settings["application_handler"]
        with mock.patch(
            "builtins.open", mock.mock_open(read_data=json.dumps(invalid_settings))
        ) as mock_file:
            resolver = SettingsResolver(self.settings_file_path)

        assert resolver._settings == invalid_settings
        with pytest.raises(KeyError):
            resolver.validate()

    def test_application_handler_returns_correct_class(self):
        self.resolver._settings = self.settings
        result = self.resolver.application_handler
        self.assertEqual(result, ApplicationHandler)

    def test_application_handler_caches_class(self):
        self.resolver._settings = self.settings
        with mock.patch("JPipe.settings._get_class") as mock_get_class:
            result1 = self.resolver.application_handler
            result2 = self.resolver.application_handler
            mock_get_class.assert_called_once_with(self.settings["application_handler"])
            self.assertEqual(result1, result2)

    def test_disk_handler_returns_correct_class(self):
        self.resolver._settings = self.settings
        result = self.resolver.disk_handler
        self.assertEqual(result, DiskHandler)

    def test_disk_handler_caches_class(self):
        self.resolver._settings = self.settings
        with mock.patch("JPipe.settings._get_class") as mock_get_class:
            result1 = self.resolver.disk_handler
            result2 = self.resolver.disk_handler
            mock_get_class.assert_called_once_with(self.settings["disk_handler"])
            self.assertEqual(result1, result2)

    def test_get_validators_returns_list_of_classes(self):
        self.resolver._settings = self.settings
        result = self.resolver.get_validators("my_app")
        expected = [ValidatorBase]
        self.assertEqual(result, expected)

    def test_get_validators_returns_empty_list_for_missing_application(self):
        self.resolver._settings = self.settings
        result = self.resolver.get_validators("unknown_app")
        self.assertEqual(result, [])

    def test_get_hooks_returns_list_of_classes(self):
        self.resolver._settings = self.settings
        result = self.resolver.get_hooks("my_app")
        expected = [ValidatorBase]
        self.assertEqual(result, expected)

    def test_get_hooks_returns_empty_list_for_missing_application(self):
        self.resolver._settings = self.settings
        result = self.resolver.get_hooks("unknown_app")
        self.assertEqual(result, [])
