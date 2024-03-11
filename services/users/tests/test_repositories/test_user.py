import pytest
import pytest_asyncio
from tests.utils.mocks import create_fake_user_credentials, USER_PASSWORD  # noqa
from app.repositories import UserRepository
from app.models import User
from app.exceptions import DuplicateEmailError


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
    async def test_create_duplicate_user(self, user):
        credentials = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "password": user.password,
        }
        with pytest.raises(DuplicateEmailError):
            await self.repository.create(**credentials)

    @pytest.mark.asyncio
    async def test_password_is_hashed_after_creation(self, user):
        assert user.password != USER_PASSWORD

    @pytest.mark.asyncio
    async def test_retrieve_user(self, user):
        retrieved_user = await self.repository.retrieve(email=user.email)
        assert retrieved_user is not None
        assert retrieved_user.email == user.email
        assert retrieved_user.first_name == user.first_name
        assert isinstance(user, User)
