from typing import Annotated

from pydantic import BaseModel, Field


class Player(BaseModel):
    id: Annotated[str, Field(min_length=1, max_length=50)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    selected: Annotated[bool, Field()] = False
    spy: Annotated[bool, Field()] = False


class LobbyCreate(BaseModel):
    id: Annotated[str, Field(min_length=1, max_length=50)]
    players: Annotated[list[Player], Field(min_items=1, max_items=30)]


class LobbyResponse(BaseModel):
    id: Annotated[str, Field(min_length=1, max_length=50)]
    players: Annotated[list[Player], Field()]


class LobbyUpdate(BaseModel):
    players: Annotated[list[Player], Field()]
