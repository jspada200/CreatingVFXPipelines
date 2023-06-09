from typing import Optional, Tuple

from .base import JPipeBase
from .application_handler import ApplicationHandler
from .disk_handler import DiskHandler


class ValidatorBase(JPipeBase):
    """
    Base class for all validators.
    """
    display_name = "ValidatorBase"

    def __init__(self, application_handler: ApplicationHandler, disk_handler: DiskHandler):
        super().__init__()
        self.application_handler = application_handler
        self.disk_handler = disk_handler

    def validate(self) -> Tuple[bool, Optional[str]]:
        """"""
        # Note: Return type tuple is only available in Python 3.9 and above.
        raise NotImplementedError("validate() must be implemented in derived class.")
