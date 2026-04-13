from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from lib.db_session import get_db
from models.schemas import TokenResponse, UserCreate, UserRead
from repository.user_repository import UserRepository
from services.auth_service import AuthService
from services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    if user_repository.get_by_email(payload.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    return UserService(db).create_user(payload.email, payload.password, payload.full_name)


@router.post("/login", response_model=TokenResponse)
def login(payload: UserCreate, db: Session = Depends(get_db)):
    user = UserRepository(db).get_by_email(payload.email)
    auth_service = AuthService()
    if not user or not auth_service.verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(access_token=auth_service.create_access_token(str(user.id)))
