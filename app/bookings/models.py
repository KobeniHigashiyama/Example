from sqlalchemy import (Column, Integer, JSON, String, ForeignKey,
                        Date,Computed)
from app.database import Base
from sqlalchemy.orm import relationship


class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_days = Column(Integer)
    total_cost = Column(Integer)
    user = relationship("Users", back_populates="booking")
    room = relationship("Rooms", back_populates="booking")

    def __str__(self):
        return f"Booking#{self.id}"




