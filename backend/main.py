import uvicorn
from fastapi import FastAPI

from lib.config import settings
from lib.logger import configure_logger, get_logger
from routes import api_router


configure_logger()
logger = get_logger(__name__)

app = FastAPI(title=settings.app_name)
app.include_router(api_router)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    logger.info("Starting API on %s:%s", settings.app_host, settings.app_port)
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_env == "local",
    )
