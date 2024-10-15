"""adding Foreign key to product table from user table 

Revision ID: b6ac4a56ec54
Revises: 1825231435f4
Create Date: 2024-10-10 16:44:59.653769

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer,ForeignKey 

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6ac4a56ec54'
down_revision: Union[str, None] = '1825231435f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products",Column("user_id",Integer,ForeignKey("user.id",ondelete="CASCADE"),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("products","user_id")
    pass
