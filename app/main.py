import uvicorn
from fastapi import FastAPI

from app.api.routes.api import router as api_router
from app.core.config import api_settings, app_settings, uvicorn_settings


def get_application() -> FastAPI:
    application = FastAPI(**api_settings.dict())
    application.include_router(api_router, prefix=app_settings.api_prefix)
    return application


app = get_application()


def main():
    uvicorn.run("main:app", **uvicorn_settings.dict())


if __name__ == "__main__":
    main()
