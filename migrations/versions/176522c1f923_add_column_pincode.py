""" add column pincode

Revision ID: 176522c1f923
Revises: 
Create Date: 2025-08-03 03:10:56.443894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '176522c1f923'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column( 'users', sa.Column('pincode', sa.String(10), nullable=True))


def downgrade() -> None:
   op.drop_column('users', 'pincode')
