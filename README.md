# Smart Expense Tracker API

A REST API built using **FastAPI** to manage personal expenses.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Delete an expense
- Interactive API documentation using Swagger UI

## Project Structure

```
expense-tracker-API/
│
├── src/
├── tests/
├── README.md
├── AI_NOTES.md
├── requirements.txt
└── pytest.ini
```

## Installation

Clone the repository:

```bash
git clone https://github.com/MdAshim/expense-tracker-API.git
cd expense-tracker-API
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## Running the Tests

```bash
python -m pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| POST | /expenses | Add a new expense |
| GET | /expenses | View all expenses |
| GET | /expenses?category=Food | Filter expenses by category |
| GET | /expenses/total | Calculate total expenses |
| DELETE | /expenses/{id} | Delete an expense |

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Pytest
- JSON file storage
