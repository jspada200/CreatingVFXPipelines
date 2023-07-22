from JPipe.hook import BaseHook
import os

class GeneratePlayblasts(BaseHook):

    def run(self):
        """
        Generate media from each of the cameras in the scene.
        """
        filename = self.application_provider.get_file_name(basename=True)
        playblast_file_name = os.path.join(self.disk_provider.get_tmp_dir(), f"{filename}_playblast.mov")

        playblast_file = self.application_provider.generate_playblast(
            playblast_file_name)
        self.checkin_controller.checkin_files.append(playblast_file)
