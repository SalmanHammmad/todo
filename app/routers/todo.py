from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_session
from .. import crud, schemas

router = APIRouter()

@router.get("/", response_model=list[schemas.TodoOut])
async def list_all(db: AsyncSession = Depends(get_session)):
    return await crud.list_todos(db)

@router.post("/", response_model=schemas.TodoOut, status_code=201)
async def create(payload: schemas.TodoCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_todo(db, title=payload.title)

@router.patch("/{todo_id}", response_model=schemas.TodoOut)
async def patch(todo_id: int, payload: schemas.TodoUpdate, db: AsyncSession = Depends(get_session)):
    item = await crud.update_todo(db, todo_id, title=payload.title, done=payload.done)
    if not item:
        raise HTTPException(404, "Not found")
    return item

@router.delete("/{todo_id}", status_code=204)
async def remove(todo_id: int, db: AsyncSession = Depends(get_session)):
    await crud.delete_todo(db, todo_id)
