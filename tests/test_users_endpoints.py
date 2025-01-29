import pytest
from httpx import ASGITransport, AsyncClient
from main import app


@pytest.mark.anyio
async def test_register_user_successfully():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/auth/register/",
            json={"username": "Karlach", "password": "screwavernus13"},
        )
    assert response.status_code == 200
    assert response.json() == {'message': 'User added successfully'}


@pytest.mark.anyio
async def test_register_user_username_taken():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/auth/register/",
            json={'username': 'Wyll', 'password': '_prideofthegate_'},
        )
    assert response.status_code == 400


@pytest.mark.anyio
async def test_login_successfully():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/auth/login/",
            json={'username': 'Wyll', 'password': '_prideofthegate_'},
        )
    assert response.status_code == 200
    assert 'access_token' in response.json()


@pytest.mark.anyio
async def test_login_unauthorized():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/auth/login/",
            json={'username': 'Gortash', 'password': 'edictofbane'},
        )
    assert response.status_code == 401
