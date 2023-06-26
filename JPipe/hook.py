import JPipe.base
from JPipe.checkin_controller import CheckinController

class BaseHook(JPipe.base.JPipeBase):
    """
    Base class for hooks that run as part of the check in process.
    """

    def __init__(self, checkin_controller: CheckinController):
        super().__init__()
        self.checkin_controller = checkin_controller
        self.application_handler = self.checkin_controller.application_controller
        self.disk_handler = self.checkin_controller.disk_handler

    def run(self):
        """Run the hook."""
        raise NotImplementedError("Hook.run() not implemented.")