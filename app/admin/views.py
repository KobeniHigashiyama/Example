from sqladmin import ModelView
from app.user.models import Users
from app.bookings.models import Booking
from app.hotels.models import Hotel
from app.hotels.rooms.models import Rooms


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.booking]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c] + [Rooms.hotel, Rooms.booking]
    name = "Номер"
    name_plural = "Номера"
    icon = "fa-solid fa-bed"


class BookingsAdmin(ModelView, model=Booking):
    column_list = [c.name for c in Booking.__table__.c] + [Booking.user, Booking.room]
    name = "Booking"
    name_plural = "Bookings"
    icon = "fa-solid fa-book"


class HotelsAdmin(ModelView, model=Hotel):
    column_list = [c.name for c in Hotel.__table__.c] + [Hotel.rooms]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"



