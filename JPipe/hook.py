import JPipe.base
from JPipe.checkin_controller import CheckinController

class BaseHook(JPipe.base.JPipeBase):
    """
    Base class for hooks that run as part of the check in process.
    """

    def __init__(self, checkin_controller: CheckinController):
        super().__init__()
        self.checkin_controller = checkin_controller
        self.application_provider = self.checkin_controller.application_provider
        self.disk_provider = self.checkin_controller.disk_provider

    def run(self):
        """Run the hook."""
        raise NotImplementedError("Hook.run() not implemented.")