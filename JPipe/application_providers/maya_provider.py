from JPipe.application_provider import ApplicationProvider
import maya.cmds as cmds


class MayaProvider(ApplicationProvider):

    default_cameras = ["frontShape", "perspShape", "sideShape", "topShape"]

    def get_all_referenced_files(self) -> list[str]:
        """
        Returns a list of all files used in the current Maya scene.
        """
        used_files = []
        file_types = ["file"]
        for file_type in file_types:
            nodes = cmds.ls(type=file_type)
            for node in nodes:
                file_path = cmds.getAttr(f"{node}.fileTextureName")
                if file_path:
                    used_files.append(file_path)
        return used_files

    def open_scene(self, file_path: str):
        """Open the provided scene file."""
        cmds.file(file_path, open=True)

    def get_file_name(self, basename=True) -> str:
        """Returns the name of the file"""
        filepath = cmds.file(query=True, sceneName=True, shortName=True)
        if basename:
            return filepath.split(".")[0]
        return filepath

    def get_all_cameras(self) -> list[str]:
        """Returns a list of all cameras in the scene"""
        return [x for x in cmds.ls(type="camera") if x not in self.default_cameras]

    def generate_playblast(self, file_path: str) -> str:
        """Generate a playblast from the provided camera."""
        cmds.playblast(
            offScreen=True,
            filename=file_path,
            forceOverwrite=True,
        )
        return file_path