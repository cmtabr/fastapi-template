"""insert_role_column_into_user_table

Revision ID: 22446453d406
Revises: f19fd0ca8bdc
Create Date: 2025-04-25 18:49:57.053599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg

from api.enums import UserRolesEnum


# revision identifiers, used by Alembic.
revision: str = '22446453d406'
down_revision: Union[str, None] = 'f19fd0ca8bdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    user_role_enum = pg.ENUM(
        *[role.value for role in UserRolesEnum],
        name='role',
        create_type=False
    )
    user_role_enum.create(op.get_bind(), checkfirst=True)
    op.add_column(
        'users',
        sa.Column('role', user_role_enum, nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users','role')
