from fastapi import Depends
from app.controllers import UserController
from app.repositories import UserRepository
from core.database import get_db


class Factory:
    """
    Factory class to create instances of controllers
    """

    @staticmethod
    def get_user_controller(db: Depends = Depends(get_db)) -> UserController:
        """
        Creates a UserController instance and returns it.
        """
        return UserController(repository=UserRepository(database_session=db))
