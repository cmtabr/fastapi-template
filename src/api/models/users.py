from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, Enum

from datetime import datetime

from api.enums import UserRolesEnum
from .shared import Base, metadata

class Users(Base):
    __tablename__ = "users"
    metadata

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, unique=True, nullable=False
    )
    username: Mapped[str] = mapped_column(String(16), nullable=True, unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    role: Mapped[UserRolesEnum] = mapped_column(
        Enum(UserRolesEnum), default=UserRolesEnum.USER
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now()
    )
    deleted_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=True
    )
