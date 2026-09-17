"""rename email to user_email

Revision ID: 03ed2ce9b1b1
Revises: 9fa37ab48001
Create Date: 2026-09-17 11:25:28.030642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03ed2ce9b1b1'
down_revision: Union[str, Sequence[str], None] = '9fa37ab48001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'email', new_column_name='user_email')

def downgrade() -> None:
    op.alter_column('users', 'user_email', new_column_name='email')
