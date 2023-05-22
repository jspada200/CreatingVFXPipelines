from .base import JPipeBase
import os


class DiskHandler(JPipeBase):
    """Handles all operations related to the file system."""

    def file_exists(self, file_path: str) -> bool:
        """Return True if the file exists, False otherwise."""
        return os.path.exists(file_path)
