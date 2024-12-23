from datetime import date
from sqlalchemy import and_, func, or_, select

from app.hotels.rooms.models import Rooms
from app.bookings.models import Booking
from app.Dao.base_dao import BaseDao
from app.database import async_session_maker


class RoomsDAO(BaseDao):
    model = Rooms

    @classmethod
    async def find_all(cls, hotel_id,date_from: date, date_to: date):

        booked_rooms = (
            select(Booking.room_id, func.count(Booking.room_id).label("rooms_booked"))
            .select_from(Booking)
            .where(
                or_(
                    and_(
                        Booking.date_from >= date_from,
                        Booking.date_from <= date_to,
                    ),
                    and_(
                        Booking.date_from <= date_from,
                        Booking.date_to > date_from,
                    ),
                ),
            )
            .group_by(Booking.room_id)
            .cte("booked_rooms")
        )

        get_rooms = (
            select(
                Rooms.__table__.columns,
                (Rooms.price * (date_to - date_from).days).label("total_cost"),
                (Rooms.quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)).label("rooms_left"),
            )
            .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
            .where(
                Rooms.hotel_id == hotel_id
            )
        )
        async with async_session_maker() as session:
            # logger.debug(get_rooms.compile(engine, compile_kwargs={"literal_binds": True}))
            rooms = await session.execute(get_rooms)
            return rooms.mappings().all()
