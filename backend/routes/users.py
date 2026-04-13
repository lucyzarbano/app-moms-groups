from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
def get_current_user_placeholder() -> dict[str, str]:
    return {"detail": "Current user profile endpoint placeholder"}
