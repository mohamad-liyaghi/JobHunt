from fastapi.exceptions import HTTPException
from fastapi import status
from typing import Union
from app.repositories import UserRepository
from app.exceptions.user import DuplicateEmailError
from core.handlers import JWTHandler, PasswordHandler


class UserController:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create(self, **kwargs):
        try:
            return await self.repository.create(**kwargs)
        except DuplicateEmailError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
            )

    async def retrieve_by_uuid(self, uuid: str):
        user = await self.repository.retrieve(uuid=uuid)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def retrieve_by_id(self, user_id):
        user = await self.repository.retrieve(id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def login_user(self, email: str, password: str) -> Union[str, None]:
        user = await self.repository.retrieve(email=email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not await PasswordHandler.verify_password(user.password, password):
            raise HTTPException(status_code=403, detail="Invalid password")

        token = await JWTHandler.create_access_token(data={"user_uuid": str(user.uuid)})
        return token
