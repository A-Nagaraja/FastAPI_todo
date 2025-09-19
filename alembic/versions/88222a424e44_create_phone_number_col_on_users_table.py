"""create phone number col on users table

Revision ID: 88222a424e44
Revises:
Create Date: 2025-09-18 20:03:40.558192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88222a424e44'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(length=15), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users','phone_number')
