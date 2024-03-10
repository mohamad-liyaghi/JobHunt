from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr = Field(..., title="User email")
    first_name: str = Field(..., title="User first name")
    last_name: str = Field(..., title="User last name")
    bio: Optional[str] = Field(..., title="User bio", max_length=120)

    class Config:
        arbitrary_types_allowed = True
