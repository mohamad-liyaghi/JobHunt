from pydantic import Field, EmailStr, BaseModel
from app.schemas.core.users import UserBase


class UserRegisterIn(UserBase):
    password: str = Field(..., title="User password")


class UserLoginIn(BaseModel):
    email: EmailStr = Field(..., title="User email")
    password: str = Field(..., title="User password")
