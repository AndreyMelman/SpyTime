import uuid

from fastapi import HTTPException, status

from models import Lobby
from .shemas import LobbyCreate, LobbyUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_lobbies(
    session: AsyncSession,
) -> list[Lobby]:
    stmt = select(Lobby).order_by(Lobby.lobby_id)
    result = await session.execute(stmt)
    lobbies = result.scalars().all()
    return list(lobbies)


async def get_lobby_by_id(
    session: AsyncSession,
    lobby_id: uuid.UUID,
) -> Lobby | None:
    stmt = select(Lobby).where(Lobby.lobby_id == lobby_id)
    result = await session.execute(stmt)
    lobby = result.scalar_one_or_none()

    return lobby


async def create_lobby(
    session: AsyncSession,
    lobby_in: LobbyCreate,
) -> Lobby | HTTPException:
    new_lobby = Lobby(**lobby_in.model_dump())
    session.add(new_lobby)
    await session.commit()
    return new_lobby


async def update_lobby(
    session: AsyncSession,
    lobby: Lobby,
    lobby_update: LobbyUpdate,
    partial: bool = False,
) -> Lobby:
    for name, value in lobby_update.model_dump(exclude_unset=partial).items():
        setattr(lobby, name, value)
    await session.commit()
    return lobby


async def clean_lobby(
    session: AsyncSession,
    lobby: Lobby,
) -> Lobby:
    lobby.players = []
    await session.commit()
    return lobby


async def delete_lobby(
    session: AsyncSession,
    lobby: Lobby,
) -> None:
    await session.delete(lobby)
    await session.commit()
