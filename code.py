from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "users.json"


# ---------------------------------------------------
# Допоміжні функції для роботи з файлом
def load_users():
    """Завантажуємо користувачів з JSON-файлу"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users: dict):
    """Зберігаємо користувачів у JSON-файл"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# ---------------------------------------------------
# Модель користувача
class User(BaseModel):
    login: str
    first_name: str
    last_name: str
    birth_year: int


# ---------------------------------------------------
# 1. Додавання нового користувача
