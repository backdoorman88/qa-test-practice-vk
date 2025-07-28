import requests 

def test_get_users():
    """
    Test retrieving the full list of users from FakeStoreAPI.
    """
    url = "https://fakestoreapi.com/users"
    response = requests.get(url)            
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        user = data[0]
        assert "id" in user
        assert "email" in user