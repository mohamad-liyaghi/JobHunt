from pydantic import Field
from datetime import datetime
from uuid import UUID
from app.schemas.core.users import UserBase


class UserRegisterOut(UserBase):
    uuid: UUID = Field(..., title="User UUID")
    date_joined: datetime = Field(..., title="User date joined")

    class Config:
        from_attriubtes = True
