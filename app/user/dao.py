from app.Dao.base_dao import BaseDao
from app.user.models import Users


class UserDao(BaseDao):
    model = Users
