from ..application_handler import ApplicationHandler
import maya.cmds as cmds


class MayaHandler(ApplicationHandler):

    def get_all_referenced_files(self) -> list[str]:
        """
        Returns a list of all files used in the current Maya scene.
        """
        used_files = []
        file_types = ["file", "texture"]
        for file_type in file_types:
            nodes = cmds.ls(type=file_type)
            for node in nodes:
                file_path = cmds.getAttr(f"{node}.fileTextureName")
                if file_path:
                    used_files.append(file_path)
        return used_files