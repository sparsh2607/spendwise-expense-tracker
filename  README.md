# Expense Tracker API

A backend REST API built with **FastAPI**, **SQLModel**, and **SQLite** to manage income, expenses, transactions, filters, and financial summaries.

This project is designed as a beginner-friendly but professional backend API project for learning real-world Python backend development.

---

## Features

* Add income and expense transactions
* View all transactions
* View a single transaction by ID
* Update transactions
* Delete transactions
* Filter transactions by category
* Filter transactions by transaction type
* Filter transactions by date range
* View overall financial summary
* View category-wise expense summary
* View monthly summary
* SQLite database integration
* Input validation
* Error handling
* Pytest-based API testing
* Interactive Swagger UI documentation

---

## Tech Stack

* Python
* FastAPI
* SQLModel
* SQLite
* Pydantic
* Pytest

---

## Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── services.py
│
├── tests/
│   ├── __init__.py
│   └── test_transactions.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sparsh2607/expense-tracker-api.git
cd expense-tracker-api
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start the development server:

```bash
fastapi dev app/main.py
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint                          | Description                       |
| ------ | --------------------------------- | --------------------------------- |
| GET    | `/`                               | Home route                        |
| POST   | `/transactions`                   | Create a new transaction          |
| GET    | `/transactions`                   | Get all transactions              |
| GET    | `/transactions/{transaction_id}`  | Get a transaction by ID           |
| PATCH  | `/transactions/{transaction_id}`  | Update a transaction              |
| DELETE | `/transactions/{transaction_id}`  | Delete a transaction              |
| GET    | `/summary`                        | Get overall financial summary     |
| GET    | `/summary/categories`             | Get category-wise expense summary |
| GET    | `/summary/monthly/{year}/{month}` | Get monthly financial summary     |

---

## Query Filters

You can filter transactions using query parameters.

Filter by category:

```text
GET /transactions?category=Food
```

Filter by transaction type:

```text
GET /transactions?transaction_type=expense
```

Filter by date range:

```text
GET /transactions?start_date=2026-07-01&end_date=2026-07-31
```

Use multiple filters together:

```text
GET /transactions?category=Food&transaction_type=expense
```

---

## Sample Transaction Request

```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "transaction_type": "expense",
  "description": "College lunch",
  "transaction_date": "2026-07-05"
}
```

---

## Sample Transaction Response

```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "transaction_type": "expense",
  "description": "College lunch",
  "transaction_date": "2026-07-05",
  "id": 1
}
```

---

## Sample Summary Response

```json
{
  "total_income": 10000,
  "total_expense": 1350,
  "balance": 8650,
  "total_transactions": 4
}
```

---

## Validation Rules

* Title must be between 2 and 100 characters
* Amount must be greater than 0
* Amount cannot be more than 1 crore
* Category must be between 2 and 50 characters
* Transaction date cannot be in the future
* Description cannot exceed 250 characters
* Transaction type must be either `income` or `expense`

---

## Running Tests

This project uses **Pytest** for API testing.

Run tests using:

```bash
pytest
```

The test suite checks:

* Home route
* Create transaction
* Get all transactions
* Get single transaction
* Update transaction
* Delete transaction
* Financial summary
* Invalid transaction validation

---

## Future Improvements

* User authentication
* JWT login system
* PostgreSQL support
* CSV export
* Budget limit feature
* Streamlit dashboard
* React frontend
* Docker support
* Deployment on Render/Railway

---

## Author

Built by **Sparsh Gahoi**.

