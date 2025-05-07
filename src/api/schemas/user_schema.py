from pydantic import BaseModel, EmailStr

from typing import Annotated

from api.enums import UserRolesEnum


class UserBaseSchema(BaseModel):
    """Base model for User schema."""
    email: Annotated[EmailStr, "User email"]
    password: Annotated[str, "Password"]


class GetUserSchema(UserBaseSchema):
    """Schema for current user."""
    username: Annotated[str, "Username"]
    role: Annotated[UserRolesEnum, "User role"]


class UserLoginSchema(UserBaseSchema):
    """Schema for user login."""
    pass


class CreateUserSchema(UserBaseSchema):
    """Schema for user creation."""
    username: Annotated[str, "Username"]


class UserUpdateSchema(UserBaseSchema):
    """Schema for user update."""
    username: str | None = None
    is_active: bool | None = None
