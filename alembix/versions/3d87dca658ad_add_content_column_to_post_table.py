"""add content column to post table

Revision ID: 3d87dca658ad
Revises: 8b5a029e47c8
Create Date: 2025-09-01 10:19:38.369992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d87dca658ad'
down_revision: Union[str, Sequence[str], None] = '8b5a029e47c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')