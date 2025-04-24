from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime

from datetime import datetime

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    metadata

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(
        String(36), primary_key=True, unique=True, nullable=False
    )
    username: Mapped[str] = mapped_column(String(16), nullable=True)
    password_hash: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now()
    )
    deleted_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=True
    )
