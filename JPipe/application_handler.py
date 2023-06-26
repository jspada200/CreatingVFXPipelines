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

    def get_file_name(self, basename=False) -> str:
        """Returns the name of the file"""
        raise NotImplementedError("get_file_name() must be implemented in derived class.")

    def get_all_cameras(self) -> list[str]:
        """Returns a list of all cameras in the scene"""
        raise NotImplementedError("get_all_cameras() must be implemented in derived class.")

    def generate_playblast(self, camera: str, file_path: str) -> str:
        """Generate a playblast from the provided camera."""
        raise NotImplementedError("generate_playblast() must be implemented in derived class.")