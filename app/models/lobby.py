import uuid

from sqlalchemy.dialects.postgresql import UUID

from core.db.base import Base
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Lobby(Base):
    __tablename__ = "lobbies"

    lobby_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    players: Mapped[list[dict]] = mapped_column(
        JSON,
        nullable=False,
        default=[],
    )

    location: Mapped[list[dict]] = mapped_column(
        JSON,
        nullable=False,
        default=[],
    )

    spies_team: Mapped[bool] = mapped_column(default=False)
