from fastapi import APIRouter, Depends, status
from app.controllers import UserController
from uuid import UUID
from app.schemas.responses.profiles import UserProfileResponse
from core.factory import Factory
from core.dependencies import AuthenticationRequired


router = APIRouter(tags=["Profiles"])


@router.get("/{user_uuid}/", status_code=status.HTTP_200_OK)
async def register_user(
    user_uuid: UUID,
    _: dict = Depends(AuthenticationRequired()),
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> UserProfileResponse:
    """Return the current user if exists otherwise return none."""
    return await user_controller.retrieve_by_uuid(user_uuid)
