from fastapi import APIRouter

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("")
def list_notifications_placeholder() -> dict[str, list]:
    return {"items": []}
