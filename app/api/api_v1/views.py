from fastapi import APIRouter, status, Depends

from core.db import db_helper
from models import Lobby
from . import crud
from sqlalchemy.ext.asyncio import AsyncSession

from .shemas import LobbyCreate, LobbyUpdate, Lobby
from .dependencies import lobby_by_id

router = APIRouter(tags=["Lobby"])


@router.get("/", response_model=list[Lobby])
async def get_lobbies(
    session: AsyncSession = Depends(db_helper.get_session),
):
    return await crud.get_lobbies(
        session=session,
    )


@router.get("/{lobby_id}/", response_model=Lobby)
async def get_lobby_by_id(
    lobby: Lobby = Depends(lobby_by_id),
):
    return lobby


@router.post(
    "/",
    response_model=Lobby,
    status_code=status.HTTP_201_CREATED,
)
async def create_lobby(
    lobby_in: LobbyCreate,
    session: AsyncSession = Depends(db_helper.get_session),
):
    return await crud.create_lobby(
        session=session,
        lobby_in=lobby_in,
    )


@router.patch("/{lobby_id}/", response_model=Lobby)
async def update_lobby(
    lobby_update: LobbyUpdate,
    lobby: Lobby = Depends(lobby_by_id),
    session: AsyncSession = Depends(db_helper.get_session),
):
    return await crud.update_lobby(
        session=session,
        lobby=lobby,
        lobby_update=lobby_update,
        partial=True,
    )


@router.put("/{lobby_id}/", response_model=Lobby)
async def clean_lobby(
    lobby: Lobby = Depends(lobby_by_id),
    session: AsyncSession = Depends(db_helper.get_session),
):
    return await crud.clean_lobby(
        session=session,
        lobby=lobby,
    )


@router.delete(
    "/{lobby_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_lobby(
    session: AsyncSession = Depends(db_helper.get_session),
    lobby: Lobby = Depends(lobby_by_id),
):
    await crud.delete_lobby(
        session=session,
        lobby=lobby,
    )
