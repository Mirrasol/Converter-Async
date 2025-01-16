from fastapi.testclient import TestClient
from main import app
from app.api.schemas.users import User
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
    assert new_user in USERS_DATA


def test_login_route():
    user_data = {'username': 'Gale', 'password': 'waterdeep888'}
    response = client.post(
        '/auth/login/',
        data=user_data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
    assert response.status_code == 200
    assert 'access_token' in response.json()


def test_show_currencies_route():
    user_data = {'username': 'Gale', 'password': 'waterdeep888'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/currency/list/', headers=authorized_headers)
    assert response.status_code == 200


def test_exchange_currency_route():
    user_data = {'username': 'Gale', 'password': 'waterdeep888'}
    exchange_data = {'from': 'MOP', 'to': 'MNT', 'amount': 10}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/currency/exchange/', params=exchange_data, headers=authorized_headers)
    assert response.status_code == 200
