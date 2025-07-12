# Fake Store API Pytest Example

This project is a practical API testing framework for students and engineers, using the [Fake Store API](https://fakestoreapi.com/docs) and [pytest](https://pytest.org/).  
It demonstrates simple, class-based test cases for all core HTTP methods (GET, POST, PUT, DELETE), using best practices such as fixtures, teardown, and Python logging.

## What is this project?

- Provides ready-to-run example tests for a public fake e-commerce API.
- Showcases professional test structure with pytest.
- Handles setup and teardown automatically for created test data.
- Perfect for students, beginners, or as a base for real-world projects.

---

## Project Structure

```
qa-test-practice/
├── pytest.ini                 # Pytest configuration for logging
├── conftest.py                # Shared fixtures and helper functions
├── data/
│   └── product_payload.json   # Example payload for POST/PUT product
└── tests/
    └── test_fakestore_api.py   # A file with API tests
```

- **`pytest.ini`**: Enables rich, always-on logging for test runs.
- **`conftest.py`**: Houses fixtures and utility functions shared by all tests.
- **`data/product_payload.json`**: Contains the JSON template used for POST/PUT product tests.
- **`tests/test_fakestoreapi.py`**: Contains all core API test cases using the class-based approach.

---

## 🖥 How to set up and run tests locally

### 1. Clone the repository (using SSH)

```bash
git clone git@github.com:your-username/qa-test-practice.git
cd qa-test-practice
```
*(Replace `your-username` with your actual GitHub username.)*

---

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
*(You need at least `pytest` and `requests` in `requirements.txt`.)*

---

### 4. Explore the structure

- Review `data/product_payload.json` for the test payload
- Look at `tests/test_fakestore_api.py` for test examples

---

### 5. Run the API tests

```bash
pytest
```
- All tests will run.
- Logs and results will be printed in the terminal thanks to `pytest.ini`.

---

### 6. (Optional) Add or modify tests

- Create new tests in `tests/`
- Use fixtures/utilities from `conftest.py` as needed
- Update `product_payload.json` to experiment with new data

---

## ✅ Notes

- No API key or authentication is needed for the Fake Store API.
- These tests **create and clean up their own test data**.
- Internet access is required to run the tests (they call a live public API).

---

## 📚 More info

- [Fake Store API Documentation](https://fakestoreapi.com/docs)
- [pytest documentation](https://docs.pytest.org/)


Added some info for fun :) 
Added some other info