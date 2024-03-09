import pytest_asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from core.database import get_db
from core.database import Base
from main import app

engine = create_async_engine("sqlite+aiosqlite:///:memory:")


async def override_get_db():
    """
    Return a TestingSessionLocal instance
    :return: TestingSessionLocal
    """
    async_session = sessionmaker(  # noqa
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db  # noqa


@pytest_asyncio.fixture(scope="session")
async def get_test_session() -> AsyncSession:
    """
    Reset database and return a session
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async for session in override_get_db():
        yield session
