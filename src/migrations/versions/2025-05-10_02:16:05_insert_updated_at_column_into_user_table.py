"""insert_updated_at_column_into_user_table

Revision ID: f44f33e3fef8
Revises: e0f84a9f28da
Create Date: 2025-05-10 02:16:04.303219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f44f33e3fef8'
down_revision: Union[str, None] = 'e0f84a9f28da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column(
            'updated_at', 
            sa.DateTime(), 
            nullable=True)
    )
    op.create_index(
        'ix_users_updated_at',
        'users',
        ['updated_at'],
        unique=False
    )

def downgrade() -> None:
    """Downgrade schema."""
    # Drop index is putted here for mere convenience and example
    # In PostgreSQL, dropping a column with an index
    # will drop the index as well
    # but in MySQL, it will not, since the index is referenced
    # by multiple columns and will not be dropped
    op.drop_index('ix_users_updated_at', 'users')
    op.drop_column('users', 'updated_at')   
