import uuid

from sqlalchemy.dialects.postgresql import UUID

from core.db.base import Base
from sqlalchemy import JSON, String
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
        default=[],
    )

    location: Mapped[list[dict]] = mapped_column(
        JSON,
    )

    spies_team: Mapped[bool] = mapped_column(default=False)

    lang: Mapped[str] = mapped_column(String(20))
