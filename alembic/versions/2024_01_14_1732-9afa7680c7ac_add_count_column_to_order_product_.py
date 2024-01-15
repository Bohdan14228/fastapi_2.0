"""add count column to order product association table

Revision ID: 9afa7680c7ac
Revises: e6f731e06dec
Create Date: 2024-01-14 17:32:04.730256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9afa7680c7ac"
down_revision: Union[str, None] = "e6f731e06dec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_product_association",
        sa.Column("count", sa.Integer(), server_default="1", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_product_association", "count")
    # ### end Alembic commands ###