from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from datetime import date
import sqlite3
import os

app = FastAPI()

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "sqlite:///./financial_advisor.db"

def get_db_connection():
    conn = sqlite3.connect("financial_advisor.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserProfile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FinancialGoal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            target_amount REAL NOT NULL,
            current_amount REAL NOT NULL,
            deadline DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES UserProfile (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transaction (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date DATE NOT NULL,
            category TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES UserProfile (id)
        )
    ''')
    conn.commit()
    conn.close()

# Seed data
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserProfile (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
    cursor.execute("INSERT INTO FinancialGoal (user_id, description, target_amount, current_amount, deadline) VALUES (?, ?, ?, ?, ?)", (1, "Buy a car", 10000, 2000, "2024-12-31"))
    cursor.execute("INSERT INTO Transaction (user_id, amount, date, category) VALUES (?, ?, ?, ?)", (1, 150.0, "2023-10-01", "Groceries"))
    conn.commit()
    conn.close()

init_db()

# Data models
class UserProfile(BaseModel):
    id: int
    name: str
    email: str

class FinancialGoal(BaseModel):
    id: int
    user_id: int
    description: str
    target_amount: float
    current_amount: float
    deadline: date

class Transaction(BaseModel):
    id: int
    user_id: int
    amount: float
    date: date
    category: str

# API Endpoints
@app.get("/api/users/{user_id}", response_model=UserProfile)
def get_user_profile(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserProfile WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserProfile(**user)

@app.post("/api/goals", response_model=FinancialGoal)
def create_financial_goal(goal: FinancialGoal):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO FinancialGoal (user_id, description, target_amount, current_amount, deadline) VALUES (?, ?, ?, ?, ?)",
        (goal.user_id, goal.description, goal.target_amount, goal.current_amount, goal.deadline)
    )
    conn.commit()
    goal_id = cursor.lastrowid
    conn.close()
    return {"id": goal_id, **goal.dict()}

@app.get("/api/transactions", response_model=List[Transaction])
def get_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Transaction")
    transactions = cursor.fetchall()
    conn.close()
    return [Transaction(**transaction) for transaction in transactions]

@app.put("/api/users/{user_id}", response_model=UserProfile)
def update_user_profile(user_id: int, user: UserProfile):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE UserProfile SET name = ?, email = ? WHERE id = ?",
        (user.name, user.email, user_id)
    )
    conn.commit()
    conn.close()
    return user

# HTML Endpoints
@app.get("/", response_class=HTMLResponse)
def read_dashboard(request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/goals", response_class=HTMLResponse)
def read_goals(request):
    return templates.TemplateResponse("goals.html", {"request": request})

@app.get("/transactions", response_class=HTMLResponse)
def read_transactions(request):
    return templates.TemplateResponse("transactions.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
def read_profile(request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
def read_settings(request):
    return templates.TemplateResponse("settings.html", {"request": request})
