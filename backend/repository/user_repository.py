from sqlalchemy import select
from sqlalchemy.orm import Session

from abstractrepository.base_repository import BaseRepository
from models.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, entity_id: int) -> User | None:
        return self.db.get(User, entity_id)

    def get_by_email(self, email: str) -> User | None:
        return self.db.scalar(select(User).where(User.email == email))

    def list(self) -> list[User]:
        return list(self.db.scalars(select(User)).all())

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
