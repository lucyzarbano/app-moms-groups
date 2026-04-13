from fastapi import APIRouter

from routes import announcements, auth, chat, events, notifications, users

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(events.router)
api_router.include_router(chat.router)
api_router.include_router(notifications.router)
api_router.include_router(announcements.router)
