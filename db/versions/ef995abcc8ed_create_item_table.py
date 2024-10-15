"""create item table

Revision ID: ef995abcc8ed
Revises: 
Create Date: 2024-10-10 15:55:09.219221

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef995abcc8ed'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("products",sa.Column("id",sa.Integer, primary_key=True,nullable=False), 
                    sa.Column("name",sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("products")
    pass
