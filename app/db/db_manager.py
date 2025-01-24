from app.api.schemas.users import User
from app.db.database_old import USERS_DATA


def add_user(user: User):
    USERS_DATA.append(dict(user))


def get_user(username: str, database: list = USERS_DATA):
    for user in database:
        if user['username'] == username:
            user_data = user
            return User(**user_data)
    return None
