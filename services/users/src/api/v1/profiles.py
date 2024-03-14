from fastapi import APIRouter, Depends, status
from app.controllers import UserController
from app.schemas.responses.profiles import UserProfileResponse
from core.factory import Factory
from core.dependencies import AuthenticationRequired


router = APIRouter(tags=["Profiles"])


@router.get("/me/", status_code=status.HTTP_200_OK)
async def register_user(
    current_user=Depends(AuthenticationRequired()),
) -> UserProfileResponse:
    """Return the current user if exists otherwise return none."""
    return current_user
