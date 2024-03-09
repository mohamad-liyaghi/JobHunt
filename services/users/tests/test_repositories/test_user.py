import pytest
import pytest_asyncio
from tests.utils.mocks import create_fake_user_credentials  # noqa
from app.repositories import UserRepository
from app.models import User
from exceptions.user import DuplicateEmailError


class TestUserRepository:
    @pytest_asyncio.fixture(autouse=True)
    async def setup(self, get_test_session):
        self.repository = UserRepository(database_session=get_test_session)
        self.credentials = await create_fake_user_credentials()

    @pytest.mark.asyncio
    async def test_create_user(self):
        user = await self.repository.create(**self.credentials)
        assert user is not None
        assert user.first_name == self.credentials.get("first_name")

    @pytest.mark.asyncio
    async def test_create_duplicate_user(self):
        user = await self.repository.create(**self.credentials)
        with pytest.raises(DuplicateEmailError):
            await self.repository.create(**self.credentials)

    @pytest.mark.asyncio
    async def test_retrieve_user(self):
        await self.repository.create(**self.credentials)
        user = await self.repository.retrieve(email=self.credentials.get("email"))
        assert user is not None
        assert user.email == user.email
        assert user.first_name == user.first_name
        assert isinstance(user, User)
