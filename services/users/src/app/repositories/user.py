from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union
from app.models import User
from app.exceptions import DuplicateEmailError
from core.handlers import PasswordHandler


class UserRepository:
    """
    User repository is responsible for handling user data.
    """

    def __init__(self, database_session: AsyncSession):
        self.model = User
        self.database_session = database_session

    async def retrieve(self, **kwargs) -> Union[User, None]:
        """
        Retrieve a user by their email address.
        """
        query = select(self.model).filter_by(**kwargs)
        result = await self.database_session.execute(query)
        return result.scalars().first()

    async def create(self, **data) -> User:
        """
        Create a new user.
        """
        email = data.get("email")
        if await self.retrieve(email=email):
            raise DuplicateEmailError

        hashed_password = await PasswordHandler.hash_password(data.pop("password"))
        data.setdefault("password", hashed_password)

        instance = self.model(**data)
        self.database_session.add(instance)
        await self.database_session.commit()
        await self.database_session.refresh(instance)
        return instance
