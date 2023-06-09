from JPipe.base import JPipeBase

class ApplicationHandler(JPipeBase):

    def get_all_referenced_files(self) -> list[str]:
        """
        Returns a list of all files used in the current scene.
        """
        raise NotImplementedError("get_all_referenced_files() must be implemented in derived class.")

    def open_scene(self, file_path: str):
        """Open the provided scene file."""
        raise NotImplementedError("open_scene_file() must be implemented in derived class.")