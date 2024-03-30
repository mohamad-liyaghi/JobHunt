from uuid import UUID
from app.schemas.core.users import UserBase


class UserProfileResponse(UserBase):
    """
    User profile response schema.
    """

    id: int

    class Config:
        from_attriubtes = True
