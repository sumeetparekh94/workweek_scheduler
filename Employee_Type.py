from enum import Enum

class Employee_Type(Enum):
    """
    Enum to handle different employee types.

    """
    CERTIFIED_INSTALLER = 1
    INSTALLER_PENDING_CERT = 2
    HANDYMEN = 3
    