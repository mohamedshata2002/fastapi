"""creating User table

Revision ID: 1825231435f4
Revises: 5a3712796eb7
Create Date: 2024-10-10 16:39:37.690028

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1825231435f4'
down_revision: Union[str, None] = '5a3712796eb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("user",Column("id",Integer, primary_key=True,nullable=False),
                    Column("name",String,nullable=False),
                    Column("email",String,nullable=False),
                    Column("password",String,nullable=False),
                    Column("time",TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
                    )
    pass


def downgrade() -> None:
    op.drop_table("user")
    pass
