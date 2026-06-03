import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_register_and_login(client):
    register_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpass123",
    }
    response = await client.post("/auth/register", json=register_data)
    assert response.status_code == 201

    login_data = {"username": "test@example.com", "password": "testpass123"}
    response = await client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
