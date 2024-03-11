from fastapi import APIRouter, Depends, status
from app.controllers import UserController
from core.factory import Factory
from app.schemas.requests.auth import UserRegisterIn, UserLoginIn
from app.schemas.responses.auth import UserRegisterOut

router = APIRouter(tags=["Authentication"])


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def register_user(
    request: UserRegisterIn,
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> UserRegisterOut:
    """Register a new user."""
    return await user_controller.create(**request.model_dump())


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    request: UserLoginIn,
    user_controller: UserController = Depends(Factory().get_user_controller),
) -> dict:
    """Login a user."""
    token = await user_controller.login_user(
        email=request.email, password=request.password
    )
    return {"access_token": token, "token_type": "bearer"}
