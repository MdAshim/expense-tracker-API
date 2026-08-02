from fastapi import APIRouter, HTTPException, status
from src.models import Expense
from src.storage import load_expenses, save_expenses
from typing import Optional
router = APIRouter()


@router.post("/expenses",status_code=status.HTTP_201_CREATED,
    summary="Add a new expense",
    description="Creates a new expense and stores it in the JSON file.")
def add_expense(expense: Expense):
    expenses = load_expenses()

    new_expense = {
        "id": len(expenses) + 1,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense

@router.get("/expenses")
def get_expenses(category: Optional[str] = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses

@router.get("/expenses/total")
def get_total_expenses(category: Optional[str] = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    if category:
        return {
            "category": category,
            "total": total
        }

    return {
        "total": total
    }

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            return {"message": "Expense deleted successfully"}

    raise HTTPException(status_code=404, detail="Expense not found")