import pytest
from unittest.mock import MagicMock
from ..validators.validate_references import ValidateReferences
@pytest.fixture
def mock_application_handler():
    mock_handler = MagicMock()
    mock_handler.get_all_referenced_files.return_value = [
        "/path/to/file1.txt",
        "/path/to/file2.txt",
        "/path/to/file3.txt"
    ]
    return mock_handler

@pytest.fixture
def mock_disk_handler():
    mock_handler = MagicMock()
    return mock_handler

def test_validate_links_with_all_files_existing(mock_application_handler, mock_disk_handler):
    mock_disk_handler.file_exists.side_effect = lambda x: True
    validator = ValidateReferences(mock_application_handler, mock_disk_handler)
    result, error = validator.validate()
    assert result == True
    assert error == None

def test_validate_links_with_some_files_missing(mock_application_handler, mock_disk_handler):
    mock_disk_handler.file_exists.side_effect = lambda x: x != "/path/to/file2.txt"
    validator = ValidateReferences(mock_application_handler, mock_disk_handler)
    result, error = validator.validate()
    assert result == False
    assert error == "The following files do not exist: ['/path/to/file2.txt']"

def test_validate_links_with_all_files_missing(mock_application_handler, mock_disk_handler):
    mock_disk_handler.file_exists.side_effect = lambda x: False
    validator = ValidateReferences(mock_application_handler, mock_disk_handler)
    result, error = validator.validate()
    assert result == False
    assert error == "The following files do not exist: ['/path/to/file1.txt', '/path/to/file2.txt', '/path/to/file3.txt']"