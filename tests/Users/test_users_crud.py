import requests
import json
import pytest

BASE_URL = "https://fakestoreapi.com/users"

def load_payload():
    with open("data/user_payload.json") as f:
        return json.load(f)

@pytest.fixture
def user_teardown():
    ids = []
    yield ids
    for uid in ids:
        requests.delete(f"{BASE_URL}/{uid}")

def test_get_users_list(user_teardown):
    resp = requests.get(BASE_URL)
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]

def test_create_user(user_teardown):
    payload = load_payload()
    resp = requests.post(BASE_URL, json=payload)
    assert resp.status_code in (200, 201)

    data = resp.json()
    user_id = data.get("id")
    assert user_id is not None
    user_teardown.append(user_id)

def test_update_user(user_teardown):
    payload = load_payload()
    post_resp = requests.post(BASE_URL, json=payload)
    assert post_resp.status_code in (200, 201)
    user_id = post_resp.json().get("id")
    assert user_id is not None
    user_teardown.append(user_id)

    update_payload = payload.copy()
    update_payload["email"] = "updated_email@example.com"
    put_resp = requests.put(f"{BASE_URL}/{user_id}", json=update_payload)
    assert put_resp.status_code == 200

    updated = put_resp.json()
    assert updated.get("email") == "updated_email@example.com"

def test_delete_user():
    payload = load_payload()
    post_resp = requests.post(BASE_URL, json=payload)
    assert post_resp.status_code in (200, 201)
    user_id = post_resp.json().get("id")
    assert user_id is not None
    del_resp = requests.delete(f"{BASE_URL}/{user_id}")
    assert del_resp.status_code == 200
    deleted = del_resp.json()
    assert deleted is None