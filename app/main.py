from fastapi import FastAPI
from .routers import todo
from .db import init_db

app = FastAPI(title="Todos API", version="1.0.0")

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

app.include_router(todo.router, prefix="/api/todos", tags=["todos"])
#commit2