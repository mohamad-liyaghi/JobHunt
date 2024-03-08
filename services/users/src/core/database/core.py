from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from core.settings import settings

engine = create_async_engine(settings.POSTGRES_URL)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)  # noqa

Base = declarative_base()
