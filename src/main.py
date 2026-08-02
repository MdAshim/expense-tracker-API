from fastapi import FastAPI
from src.routes import router

app = FastAPI(title="Smart Expense Tracker API")

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }