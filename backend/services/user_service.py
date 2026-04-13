from sqlalchemy.orm import Session

from models.user import User
from repository.user_repository import UserRepository
from services.auth_service import AuthService


class UserService:
    def __init__(self, db: Session) -> None:
        self.user_repository = UserRepository(db)
        self.auth_service = AuthService()

    def create_user(self, email: str, password: str, full_name: str | None = None) -> User:
        hashed_password = self.auth_service.hash_password(password)
        user = User(email=email, hashed_password=hashed_password, full_name=full_name)
        return self.user_repository.create(user)
