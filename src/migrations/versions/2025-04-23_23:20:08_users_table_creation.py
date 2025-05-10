"""User table creation

Revision ID: f19fd0ca8bdc
Revises: 
Create Date: 2025-04-23 23:20:08.216626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f19fd0ca8bdc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'user_id', name='pk_users'),
    sa.UniqueConstraint('user_id', name='uq_user_id'),
    sa.UniqueConstraint('username', name='uq_username'),
    sa.UniqueConstraint('email', name='uq_email'),
    sa.CheckConstraint('deleted_at IS NULL OR deleted_at > created_at', name='check_deleted_at')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
