from fastapi import Depends, status, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.models import User
from core.factory import Factory
from app.controllers import UserController


class AuthenticationRequired:
    """
    Check if the user is authenticated.
    If the user is not authenticated, raise an HTTPException otherwise return the user.
    """

    async def __call__(
        self,
        request: Request,
        token: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
        user_controller: UserController = Depends(Factory().get_user_controller),
    ) -> User:
        """
        Check if user is authenticated and return the user.
        """
        if not token:
            raise HTTPException(
                detail="Authentication required", status_code=status.HTTP_403_FORBIDDEN
            )
        print(request.user)

        return await user_controller.retrieve_by_id(request.user.id)
