import requests
import json

def test_delete_users():
    """
    Test deleting a user via DELETE /users/{id}.
    """
    base_url = "https://fakestoreapi.com/users"
    with open("data/user_payload.json") as f:
        payload = json.load(f)
    post_resp = requests.post(base_url, json=payload)
    assert post_resp.status_code in (200, 201)
    user_id = post_resp.json().get("id")
    assert user_id is not None

    del_resp = requests.delete(f"{base_url}/{user_id}")
    assert del_resp.status_code == 200
    deleted = del_resp.json()
    assert isinstance(deleted, dict)
    assert deleted.get("id") == user_id