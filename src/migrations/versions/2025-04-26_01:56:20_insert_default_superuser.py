"""insert_default_superuser

Revision ID: e0f84a9f28da
Revises: 22446453d406
Create Date: 2025-04-26 01:56:18.919345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy.types import Integer, String, Boolean, DateTime
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime
from uuid import uuid4
from api.enums import UserRolesEnum


# revision identifiers, used by Alembic.
revision: str = 'e0f84a9f28da'
down_revision: Union[str, None] = '22446453d406'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    users_table = table(
        "users",
        column("id", Integer),
        column("user_id", String),
        column("username", String),
        column("password", String),
        column("email", String),
        column("role", pg.ENUM(
            *[role.value for role in UserRolesEnum],
            name='role',
            create_type=False
        )),
        column("is_active", Boolean),
        column("created_at", DateTime),

    )
    op.bulk_insert(
        users_table,
        [
            {
                'user_id': uuid4(),
                'username': 'superuser',
                'password': 'password',
                'email': 'admin@admin.com',
                'role': 'ADMIN',
                'is_active': True,
                'created_at': datetime.now()
            }
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    users_table = table(
        "users",
        column("id", Integer),
        column("user_id", String),
        column("username", String),
        column("password", String),
        column("email", String),
        column("role", pg.ENUM(
            *[role.value for role in UserRolesEnum],
            name='role',
            create_type=False
        )),
        column("is_active", Boolean),
        column("created_at", DateTime),
        column("deleted_at", DateTime)
    )
    op.execute(
        users_table
        .delete()
        .where(users_table.c.username == 'superuser')
    )
