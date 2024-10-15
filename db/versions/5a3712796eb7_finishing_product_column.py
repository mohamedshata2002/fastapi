"""Finishing Product column

Revision ID: 5a3712796eb7
Revises: f9e2051ae172
Create Date: 2024-10-10 16:29:02.629524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean, Column
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
# revision identifiers, used by Alembic.
revision: str = '5a3712796eb7'
down_revision: Union[str, None] = 'f9e2051ae172'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products",Column("is_sale",Boolean,nullable=False,server_default="False"))
    op.add_column("products",Column("time",TIMESTAMP(timezone=True),nullable=False,server_default=text("now()")))
   
    pass


def downgrade() -> None:
    op.drop_column("is_sale")
    op.drop_column("time")
    pass
