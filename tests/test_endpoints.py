from fastapi.testclient import TestClient
from main import app
from app.db.database import USERS_DATA

client = TestClient(app)


def test_register_user_route():
    new_user = {'username': 'Wyll', 'password': 'prideofthegate'}
    response = client.post(
        '/auth/register/',
        json=new_user,
        )
    assert response.status_code == 200
    assert response.json() == {'message': 'You have successfully registered!'}
    assert new_user in USER_DATA


def test_login_route():
    response = client.post('/auth/login/')
