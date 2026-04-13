from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from lib.config import settings


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def hash_password(self, password: str) -> str:
        return password_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)

    def create_access_token(self, subject: str) -> str:
        expires_at = datetime.now(timezone.utc) + timedelta(
            minutes=settings.jwt_access_token_expire_minutes
        )
        payload = {"sub": subject, "exp": expires_at}
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
