from hodrl import api
from fastapi.testclient import TestClient

import pytest

@pytest.fixture
def client():
    client = TestClient(api.app)
    return client

def test_get_all_assets(client, all_assets):
    response = client.get("/assets")
    assert response.status_code == 200
    assert response.json() == all_assets
