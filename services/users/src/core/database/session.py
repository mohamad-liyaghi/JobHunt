from sqlalchemy.ext.asyncio import AsyncSession
from .core import async_session


async def get_db() -> AsyncSession:
    """Return a database session."""
    async with async_session() as session:
        yield session
