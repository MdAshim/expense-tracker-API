import json
from pathlib import Path

# Path to the JSON file
DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    """Read all expenses from the JSON file."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)