from typing import TYPE_CHECKING

from core.db.base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .lobby import Lobby


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(default=None, primary_key=True)
    name: Mapped[str] = mapped_column()
    selected: Mapped[bool] = mapped_column(default=False)
    spy: Mapped[bool] = mapped_column(default=False)

    lobby_id: Mapped[str] = mapped_column(ForeignKey("lobbies.id"))

    lobby: Mapped["Lobby"] = relationship(back_populates="players")
