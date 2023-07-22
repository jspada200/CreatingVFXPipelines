from ..disk_provider import DiskProvider
import os
import tempfile

class LocalDiskProvider(DiskProvider):
    """
    Handler for local disk operations.
    """

    def file_exists(self, file_path: str) -> bool:
        """Return True if the file exists, False otherwise."""
        return os.path.exists(file_path)

    def get_tmp_dir(self) -> str:
        """Get a path to the systems tmp dir"""
        return tempfile.gettempdir()