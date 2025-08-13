import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

from api import router as api_router
from create_fastapi_app import create_app

main_app = create_app()

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
main_app.include_router(api_router)


def main():
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
