"""create tables lobbies

Revision ID: 3b2e7fba2a1a
Revises: 
Create Date: 2025-01-23 01:22:43.965658

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "3b2e7fba2a1a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "lobbies",
        sa.Column(
            "lobby_id",
            sa.UUID(),
            nullable=False,
        ),
        sa.Column(
            "players",
            sa.JSON(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("lobby_id"),
    )


def downgrade() -> None:
    op.drop_table("lobbies")
