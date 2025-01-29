from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base
import datetime


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=False,
        server_default=func.now(),
    )
