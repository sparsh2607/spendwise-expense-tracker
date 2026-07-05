# Expense Tracker API

A REST API built with **FastAPI** and **SQLModel** to manage income, expenses, categories, and financial summaries.

This project helps users track their financial transactions, view spending by category, and generate monthly summaries.

## Features

* Add income and expense transactions
* View all transactions
* View a single transaction by ID
* Update existing transactions
* Delete transactions
* Filter transactions by category
* Filter transactions by transaction type
* Filter transactions by date range
* View overall financial summary
* View category-wise expense summary
* View monthly financial summary
* SQLite database integration
* Input validation and error handling
* Interactive API documentation using Swagger UI

## Tech Stack

* Python
* FastAPI
* SQLModel
* SQLite
* Pydantic

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
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker-api.git
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

Run the server:

```bash
fastapi dev app/main.py
```

Open the API docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint                          | Description                       |
| ------ | --------------------------------- | --------------------------------- |
| GET    | `/`                               | Home route                        |
| POST   | `/transactions`                   | Create a new transaction          |
| GET    | `/transactions`                   | Get all transactions              |
| GET    | `/transactions/{transaction_id}`  | Get transaction by ID             |
| PATCH  | `/transactions/{transaction_id}`  | Update transaction                |
| DELETE | `/transactions/{transaction_id}`  | Delete transaction                |
| GET    | `/summary`                        | Get overall financial summary     |
| GET    | `/summary/categories`             | Get category-wise expense summary |
| GET    | `/summary/monthly/{year}/{month}` | Get monthly financial summary     |

## Query Filters

You can filter transactions using query parameters:

```text
GET /transactions?category=Food
GET /transactions?transaction_type=expense
GET /transactions?start_date=2026-07-01&end_date=2026-07-31
GET /transactions?category=Food&transaction_type=expense
```

## Sample Request

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

## Sample Response

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

## Summary Response Example

```json
{
  "total_income": 10000,
  "total_expense": 1350,
  "balance": 8650,
  "total_transactions": 4
}
```

## Validation Rules

* Title must be between 2 and 100 characters
* Amount must be greater than 0
* Amount cannot be more than 1 crore
* Category must be between 2 and 50 characters
* Transaction date cannot be in the future
* Description cannot exceed 250 characters
* Transaction type must be either `income` or `expense`

## Future Improvements

* User authentication
* JWT login system
* PostgreSQL support
* Expense budget limit
* CSV export
* Dashboard frontend
* Unit testing with Pytest
* Docker support

## Author

Built by Sparsh Gahoi.
