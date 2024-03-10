import pytest
from httpx import AsyncClient
import pytest_asyncio
from fastapi import status
from tests.utils.mocks import create_fake_user_credentials  # noqa


@pytest.mark.asyncio
class TestRegisterRoute:
    @pytest_asyncio.fixture(autouse=True)
    async def setup_method(self, client: AsyncClient) -> None:
        credential = await create_fake_user_credentials()
        self.data = {
            "email": credential["email"],
            "first_name": credential["first_name"],
            "last_name": credential["last_name"],
            "bio": credential["bio"],
            "password": credential["password"],
        }
        self.client = client
        self.url = "v1/auth/register/"

    @pytest.mark.asyncio
    async def test_register_user_valid_data(self) -> None:
        response = await self.client.post(self.url, json=self.data)
        print(response)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.asyncio
    async def test_register_user_invalid_data(self) -> None:
        response = await self.client.post(self.url)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.asyncio
    async def test_register_user_exists_fails(self, user):
        self.data["email"] = user.email
        response = await self.client.post(self.url, json=self.data)
        assert response.status_code == status.HTTP_409_CONFLICT
