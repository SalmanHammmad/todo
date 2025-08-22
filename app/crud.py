from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Todo

async def list_todos(db: AsyncSession):
    result = await db.execute(select(Todo).order_by(Todo.id.desc()))
    return result.scalars().all()

async def create_todo(db: AsyncSession, title: str):
    todo = Todo(title=title, done=False)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

async def update_todo(db: AsyncSession, todo_id: int, *, title=None, done=None):
    values = {}
    if title is not None: values["title"] = title
    if done is not None: values["done"] = done
    if not values: return None
    await db.execute(update(Todo).where(Todo.id == todo_id).values(**values))
    await db.commit()
    return await get_todo(db, todo_id)

async def get_todo(db: AsyncSession, todo_id: int):
    return await db.get(Todo, todo_id)

async def delete_todo(db: AsyncSession, todo_id: int):
    await db.execute(delete(Todo).where(Todo.id == todo_id))
    await db.commit()
