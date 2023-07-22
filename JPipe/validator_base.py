from typing import Optional, Tuple

from .base import JPipeBase
from .application_provider import ApplicationProvider
from .disk_provider import DiskProvider


class ValidatorBase(JPipeBase):
    """
    Base class for all validators.
    """
    display_name = "ValidatorBase"

    def __init__(self, application_provider: ApplicationProvider, disk_provider: DiskProvider):
        super().__init__()
        self.application_provider = application_provider
        self.disk_provider = disk_provider

    def validate(self) -> Tuple[bool, Optional[str]]:
        """"""
        # Note: Return type tuple is only available in Python 3.9 and above.
        raise NotImplementedError("validate() must be implemented in derived class.")
