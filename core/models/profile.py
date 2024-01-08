from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    firstname: Mapped[str | None] = mapped_column(String(40))
    lastname: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]
