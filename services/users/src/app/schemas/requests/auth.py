from pydantic import Field
from app.schemas.core.users import UserBase


class UserRegisterIn(UserBase):
    password: str = Field(..., title="User password")
