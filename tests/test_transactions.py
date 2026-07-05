import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session, create_engine

from app.database import get_session
from app.main import app


test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


def get_test_session():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_session] = get_test_session

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_database():
    SQLModel.metadata.create_all(test_engine)
    yield
    SQLModel.metadata.drop_all(test_engine)


def test_home_route():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Expense Tracker API"


def test_create_transaction():
    transaction_data = {
        "title": "Lunch",
        "amount": 250,
        "category": "Food",
        "transaction_type": "expense",
        "description": "College lunch"
    }

    response = client.post("/transactions", json=transaction_data)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Lunch"
    assert data["amount"] == 250
    assert data["category"] == "Food"
    assert data["transaction_type"] == "expense"
    assert data["id"] == 1


def test_get_all_transactions():
    transaction_data = {
        "title": "Freelance Payment",
        "amount": 5000,
        "category": "Freelance",
        "transaction_type": "income",
        "description": "Client payment"
    }

    client.post("/transactions", json=transaction_data)

    response = client.get("/transactions")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Freelance Payment"


def test_get_single_transaction():
    transaction_data = {
        "title": "Shoes",
        "amount": 2500,
        "category": "Shopping",
        "transaction_type": "expense",
        "description": "Nike shoes"
    }

    create_response = client.post("/transactions", json=transaction_data)
    transaction_id = create_response.json()["id"]

    response = client.get(f"/transactions/{transaction_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Shoes"


def test_update_transaction():
    transaction_data = {
        "title": "Tea",
        "amount": 20,
        "category": "Food",
        "transaction_type": "expense",
        "description": "Evening tea"
    }

    create_response = client.post("/transactions", json=transaction_data)
    transaction_id = create_response.json()["id"]

    update_data = {
        "amount": 30,
        "description": "Updated tea price"
    }

    response = client.patch(f"/transactions/{transaction_id}", json=update_data)

    assert response.status_code == 200
    assert response.json()["amount"] == 30
    assert response.json()["description"] == "Updated tea price"


def test_delete_transaction():
    transaction_data = {
        "title": "Bus Ticket",
        "amount": 50,
        "category": "Travel",
        "transaction_type": "expense",
        "description": "College travel"
    }

    create_response = client.post("/transactions", json=transaction_data)
    transaction_id = create_response.json()["id"]

    response = client.delete(f"/transactions/{transaction_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Transaction deleted successfully"

    get_response = client.get(f"/transactions/{transaction_id}")

    assert get_response.status_code == 404


def test_financial_summary():
    income_data = {
        "title": "Freelance Payment",
        "amount": 10000,
        "category": "Freelance",
        "transaction_type": "income",
        "description": "Client payment"
    }

    expense_data = {
        "title": "Lunch",
        "amount": 250,
        "category": "Food",
        "transaction_type": "expense",
        "description": "College lunch"
    }

    client.post("/transactions", json=income_data)
    client.post("/transactions", json=expense_data)

    response = client.get("/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_income"] == 10000
    assert data["total_expense"] == 250
    assert data["balance"] == 9750
    assert data["total_transactions"] == 2


def test_invalid_transaction_amount():
    transaction_data = {
        "title": "Lunch",
        "amount": 0,
        "category": "Food",
        "transaction_type": "expense",
        "description": "Invalid amount"
    }

    response = client.post("/transactions", json=transaction_data)

    assert response.status_code == 422