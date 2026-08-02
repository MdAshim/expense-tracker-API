from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 120,
            "category": "Food",
            "date": "2026-08-02"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Coffee"


def test_get_expenses():
    
    response = client.post(
        "/expenses",
        json={
            "title": "Delete Me",
            "amount": 50,
            "category": "Test",
            "date": "2026-08-02"
        }
    )

    expense_id = response.json()["id"]

    # Delete it
    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200
def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200

def test_filter_by_category():
    response = client.get("/expenses?category=Food")
    assert response.status_code == 200