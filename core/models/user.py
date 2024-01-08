from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)  # mapped_column(unique=True) столбец уникальный

    posts: Mapped[list["Post"]] = relationship(back_populates="user")