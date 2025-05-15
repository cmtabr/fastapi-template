from enum import Enum


class UserRolesEnum(str, Enum):
    """User roles in the system."""
    ADMIN = "ADMIN"
    USER = "USER"
