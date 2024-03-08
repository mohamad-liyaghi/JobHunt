from sqlalchemy import Column, Integer, String, Boolean, DateTime
from uuid import uuid4
from core.types import CustomUUID
from typing import Optional
from datetime import datetime
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    uuid: CustomUUID = Column(String, default=uuid4, unique=True, index=True)
    email: str = Column(String, unique=True, index=True)
    first_name: str = Column(String(25), nullable=False)
    last_name: Optional[str] = Column(String(25), nullable=True)
    bio: Optional[str] = Column(String(255), nullable=True)
    date_joined: datetime = Column(DateTime, default=datetime.utcnow)
    password: str = Column(String)

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
