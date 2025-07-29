import requests
import json
from conftest import user_teardown

def test_put_users(user_teardown):
    """
    Test updating an existing user via PUT /users/{id}.
    """
    base_url = "https://fakestoreapi.com/users"
    
    with open("data/user_payload.json") as f:
        payload = json.load(f)
    post_resp = requests.post(base_url, json=payload)
    assert post_resp.status_code in (200, 201)
    user_id = post_resp.json().get("id")
    assert user_id is not None
    
    user_teardown(user_id)

    updated = payload.copy()
    updated["name"] = "UpdatedName"
    
    put_url = f"{base_url}/{user_id}"
    put_resp = requests.put(put_url, json=updated)
    assert put_resp.status_code == 200
    
    data = put_resp.json()
    assert data.get("name") == "UpdatedName"