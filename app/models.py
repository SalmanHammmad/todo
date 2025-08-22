from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String
from .db import Base

class Todo(Base):
    __tablename__ = "todos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), index=True)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
