from datetime import date

from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.user.models import Users
from app.user.dependencies import get_current_user
from app.exceptions import RoomCannotBeBooked
from app.tasks.task import send_booking_email
from pydantic import parse_obj_as
from fastapi import BackgroundTasks


router = APIRouter(
    prefix="/bookings", tags=["Бронирование"]
)


@router.get("")
async def get_booking(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)) :
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
    return booking


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)