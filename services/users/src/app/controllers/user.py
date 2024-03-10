from fastapi.exceptions import HTTPException
from fastapi import status
from app.repositories import UserRepository
from app.exceptions.user import DuplicateEmailError


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

    async def retrieve_by_id(self, user_id):
        user = await self.repository.retrieve(id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
