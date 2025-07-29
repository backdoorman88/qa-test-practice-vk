import pytest
import requests
import logging

@pytest.fixture
def user_teardown():
    created_ids = []
    def _register(uid):
        created_ids.append(uid)
    yield _register
    for uid in created_ids:
        url = f"https://fakestoreapi.com/users/{uid}"
        response = requests.delete(url)
        logging.info(f"Teardown DELETE {url}: {response.status_code}")
