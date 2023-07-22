from .base import JPipeBase


class DiskProvider(JPipeBase):
    """Handles all operations related to the file system."""

    def file_exists(self, file_path: str) -> bool:
        raise NotImplementedError("Must implement in a derived class.")

    def get_tmp_dir(self) -> str:
        """
        Get a path to the temp dir on the file system.
        """
        raise NotImplementedError("Must implement in a derived class.")
