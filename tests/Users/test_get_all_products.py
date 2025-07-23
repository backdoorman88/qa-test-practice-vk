import requests

def test_get_all_products():
    """Test retrieving the full list of products."""
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    # Перевіряємо, що отримали список, а не щось інше
    assert isinstance(data, list)
    # Якщо в нас є щонайменше один продукт, перевіряємо структуру першого
    if data:
        first = data[0]
        assert "id" in first
        assert "title" in first