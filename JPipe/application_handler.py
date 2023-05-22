from .base import JPipeBase
import maya.cmds as cmds


class ApplicationHandler(JPipeBase):

    def get_all_referenced_files(self) -> list[str]:
        """
        Returns a list of all files used in the current scene.
        """
        raise NotImplementedError("get_all_referenced_files() must be implemented in derived class.")