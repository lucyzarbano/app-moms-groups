from fastapi import APIRouter

router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.get("")
def list_announcements_placeholder() -> dict[str, list]:
    return {"items": []}
