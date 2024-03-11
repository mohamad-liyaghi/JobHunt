import pytest
from fastapi import status
from httpx import AsyncClient
from tests.utils.mocks import USER_PASSWORD  # noqa


@pytest.mark.asyncio
class TestLoginRoute:
    @pytest.fixture(autouse=True)
    def setup_method(self, client: AsyncClient, user) -> None:
        self.user = user
        self.data = {"email": user.email, "password": "default"}
        self.client = client
        self.url = "v1/auth/login"

    @pytest.mark.asyncio
    async def test_login_with_valid_credentials(self, get_test_session) -> None:
        self.data["password"] = USER_PASSWORD
        await get_test_session.refresh(self.user)
        response = await self.client.post(self.url, json=self.data)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.asyncio
    async def test_login_invalid_password(self) -> None:
        self.data["password"] = "invalid_password"
        response = await self.client.post(self.url, json=self.data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.asyncio
    async def test_login_invalid_data(self) -> None:
        response = await self.client.post(self.url)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.asyncio
    async def test_login_user_not_exist(self) -> None:
        self.data["email"] = self.data["email"] + "invalid"
        response = await self.client.post(self.url, json=self.data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
