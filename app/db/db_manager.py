from app.api.schemas.users import User
from app.db.database import USERS_DATA


def get_user(username: str, database: list = USERS_DATA):
    for user in database:
        if user['username'] == username:
            user_data = user
            return User(**user_data)
    return None
