from fastapi import FastAPI
from app.api.search.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Website Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 Allow all during development. Be careful for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
