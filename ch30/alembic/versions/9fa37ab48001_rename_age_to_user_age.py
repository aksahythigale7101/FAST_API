"""rename age to user_age

Revision ID: 9fa37ab48001
Revises: 58c7df676aed
Create Date: 2026-09-17 11:18:46.824810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fa37ab48001'
down_revision: Union[str, Sequence[str], None] = '58c7df676aed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
