import uuid
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict


class Player(BaseModel):
    id: Annotated[str, Field(min_length=1, max_length=50)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    selected: Annotated[bool, Field()] = False
    spy: Annotated[bool, Field()] = False


class LobbyBase(BaseModel):
    players: Annotated[list[Player], Field()]


class LobbyCreate(LobbyBase):
    pass


class LobbyUpdate(LobbyBase):
    pass


class Lobby(LobbyBase):
    model_config = ConfigDict(from_attributes=True)

    lobby_id: Annotated[uuid.UUID, Field()]
