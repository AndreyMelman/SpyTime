from typing import TYPE_CHECKING

from core.db.base import Base
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from .player import Player
#
# if TYPE_CHECKING:
#     from .player import Player


class Lobby(Base):
    __tablename__ = "lobbies"

    id: Mapped[str] = mapped_column(
        primary_key=True,
        index=True,
    )
    players: Mapped[list[dict]] = mapped_column(JSON, nullable=False)
