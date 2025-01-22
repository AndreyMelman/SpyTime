from typing import AsyncGenerator

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from core.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        try:
            await self.engine.dispose()
        except SQLAlchemyError as e:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
            )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        try:
            async with self.session_factory() as session:
                yield session
        except SQLAlchemyError:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error"
            )


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
)
