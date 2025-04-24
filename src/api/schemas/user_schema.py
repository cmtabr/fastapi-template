from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    """Base model for User schema."""
    email: EmailStr
    password: str


class UserLoginSchema(UserBaseSchema):
    """Schema for user login."""
    pass
