from ..disk_handler import DiskHandler
import os
import tempfile

class LocalDiskHandler(DiskHandler):
    """
    Handler for local disk operations.
    """

    def file_exists(self, file_path: str) -> bool:
        """Return True if the file exists, False otherwise."""
        return os.path.exists(file_path)

    def get_tmp_dir(self) -> str:
        """Get a path to the systems tmp dir"""
        return tempfile.gettempdir()
