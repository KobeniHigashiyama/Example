
from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.orm import relationship

from app.database import Base


class Hotel(Base):
    __tablename__ = "hotels"
    name = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, )
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    rooms = relationship("Rooms", back_populates="hotel")

    def __str__(self):
        return f"Hotel {self.name} {self.location[:30]}"
