"""create price column

Revision ID: f9e2051ae172
Revises: ef995abcc8ed
Create Date: 2024-10-10 16:06:52.909945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9e2051ae172'
down_revision: Union[str, None] = 'ef995abcc8ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products",sa.Column("price",sa.Float,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("products","price")
    pass
