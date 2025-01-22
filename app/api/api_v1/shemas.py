from pydantic import BaseModel


class Player(BaseModel):
    name: str
    selected: bool = False
    spy: bool = False


class LobbyCreate(BaseModel):
    id: str
    players: list[Player]


class LobbyResponse(BaseModel):
    id: str
    players: list[Player]


class LobbyUpdate(BaseModel):
    players: list[Player]
