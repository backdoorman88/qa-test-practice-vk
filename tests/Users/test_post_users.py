import requests
import json
import pytest
from conftest import user_teardown

def test_post_users(user_teardown):
    """
    Test creating a new user via POST /users.
    """
    url = "https://fakestoreapi.com/users"
    with open("data/user_payload.json") as f:
        payload = json.load(f)

    response = requests.post(url, json=payload)
    assert response.status_code in (200, 201)

    data = response.json()
    user_id = data.get("id")
    assert user_id is not None

    user_teardown(user_id)