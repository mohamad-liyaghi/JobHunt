import pytest
import pytest_asyncio
from fastapi import HTTPException
from tests.utils.mocks import create_fake_user_credentials, USER_PASSWORD  # noqa
from app.repositories import UserRepository
from app.controllers import UserController
from app.models import User


class TestUserController:
    @pytest_asyncio.fixture(autouse=True)
    async def setup(self, get_test_session):
        self.controller = UserController(
            UserRepository(database_session=get_test_session)
        )
        self.credentials = await create_fake_user_credentials()

    @pytest.mark.asyncio
    async def test_create_user(self):
        user = await self.controller.create(**self.credentials)
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
        with pytest.raises(HTTPException):
            await self.controller.create(**credentials)

    @pytest.mark.asyncio
    async def test_retrieve_user(self, user):
        user = await self.controller.retrieve_by_id(user.id)
        assert user is not None
        assert user.email == user.email
        assert user.first_name == user.first_name
        assert isinstance(user, User)

    @pytest.mark.asyncio
    async def test_retrieve_user_not_found(self):
        with pytest.raises(HTTPException):
            await self.controller.retrieve_by_id(0)

    @pytest.mark.asyncio
    async def test_login_with_valid_credentials(self, user):
        access_token = await self.controller.login_user(user.email, USER_PASSWORD)
        assert access_token is not None
        assert isinstance(access_token, str)

    @pytest.mark.asyncio
    async def test_login_with_invalid_password_fails(self, user):
        invalid_password = USER_PASSWORD + "invalid"
        with pytest.raises(HTTPException):
            await self.controller.login_user(user.email, invalid_password)

    @pytest.mark.asyncio
    async def test_login_with_invalid_email_fails(self, user):
        invalid_email = user.email + "invalid"
        with pytest.raises(HTTPException):
            await self.controller.login_user(invalid_email, USER_PASSWORD)

    @pytest.mark.asyncio
    async def test_retrieve_by_uuid(self, user):
        user = await self.controller.retrieve_by_uuid(user.uuid)
        assert user is not None
        assert user.email == user.email
        assert user.first_name == user.first_name
        assert isinstance(user, User)
