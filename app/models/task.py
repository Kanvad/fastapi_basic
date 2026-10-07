from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.models.owner import Owner

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
    owner_id: Mapped[int | None] = mapped_column(
        ForeignKey("owners.id"),
        nullable=True,
    )

    owner: Mapped["Owner | None"] = relationship(
        "Owner",
        back_populates="tasks",
    )