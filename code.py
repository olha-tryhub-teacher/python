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



# 2. Редагування користувача
@app.put("/user/edit/{login}")
def edit_user(login: str, new_data: User):
    users = load_users()
    if login not in users:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    users[login] = new_data.dict()
    save_users(users)
    return {"message": f"Користувача {login} оновлено", "data": new_data}


# ---------------------------------------------------
# 3. Видалення користувача
@app.delete("/user/delete/{login}")
def delete_user(login: str):
    users = load_users()
    if login not in users:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    del users[login]
    save_users(users)
    return {"message": f"Користувача {login} видалено"}


# ---------------------------------------------------
# 4. Отримання користувача за логіном
@app.get("/user/{login}")
def get_user(login: str):
    users = load_users()
    if login not in users:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")
    return users[login]


# ---------------------------------------------------
# 5. Отримання всіх користувачів (HTML)
@app.get("/users")
def get_all_users():
    users = load_users()
    if not users:
        html = "<h3>Список користувачів порожній</h3>"
    else:
        rows = ""
        for login, data in users.items():
            rows += f"<tr><td>{login}</td><td>{data['first_name']}</td><td>{data['last_name']}</td><td>{data['birth_year']}</td></tr>"

        html = f"""
        <html>
            <head><title>Список користувачів</title></head>
            <body>
                <h2>Усі користувачі</h2>
                <table border="1">
                    <tr><th>Логін</th><th>Ім'я</th><th>Прізвище</th><th>Рік народження</th></tr>
                    {rows}
                </table>
            </body>
        </html>
        """
    return HTMLResponse(content=html)
