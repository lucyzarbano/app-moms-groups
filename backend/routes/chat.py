from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.get("/groups")
def list_chat_groups_placeholder() -> dict[str, list]:
    return {"items": []}
