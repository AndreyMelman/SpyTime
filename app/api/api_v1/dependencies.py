import uuid
from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import db_helper
from models import Lobby
from . import crud


async def lobby_by_id(
    lobby_id: Annotated[uuid.UUID, Path],
    session: AsyncSession = Depends(db_helper.get_session),
) -> Lobby:
    lobby = await crud.get_lobby_by_id(
        session=session,
        lobby_id=lobby_id,
    )
    if lobby is not None:
        return lobby

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Lobby {lobby_id} not found"
    )
