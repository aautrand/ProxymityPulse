# declarative base class
from datetime import datetime

from sqlalchemy import DateTime, VARCHAR, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship

Base = declarative_base()


# Define the Friend table
class Friend(Base):
    __tablename__ = 'friend'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mac_address: Mapped[str] = mapped_column(VARCHAR(17))  # MAC addresses are 17 characters long
    disabled: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationship to link to Detection table
    detections: Mapped[list["Detection"]] = relationship("Detection", back_populates="friend", cascade="all, delete-orphan")


# Define the Detection table
class Detection(Base):
    __tablename__ = 'detection'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    detected_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    friend_id: Mapped[int] = mapped_column(ForeignKey('friends.id'))

    # Relationship back to Friend table
    friend: Mapped["Friend"] = relationship("Friend", back_populates="detections")


