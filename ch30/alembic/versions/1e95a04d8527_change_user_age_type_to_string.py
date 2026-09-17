"""change user_age type to string

Revision ID: 1e95a04d8527
Revises: 03ed2ce9b1b1
Create Date: 2026-09-17 11:40:01.197722

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1e95a04d8527"
down_revision: Union[str, Sequence[str], None] = "03ed2ce9b1b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column(
            "user_age",
            existing_type=sa.Integer(),
            type_=sa.String(50),
            existing_nullable=False,
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column(
            "user_age",
            existing_type=sa.String(50),
            type_=sa.Integer(),
            existing_nullable=False,
        )