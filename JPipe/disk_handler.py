from .base import JPipeBase


class DiskHandler(JPipeBase):
    """Handles all operations related to the file system."""

    def file_exists(self, file_path: str) -> bool:
        raise NotImplementedError("Must implement in a derived class.")