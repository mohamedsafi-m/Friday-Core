from fastapi import FastAPI
from database import cursor, conn
from pydantic import BaseModel


app = FastAPI(
    title="F.R.I.D.A.Y API",
    version="1.0.0"
)

class Memory(BaseModel):
    user_id: int
    key: str
    value: str

@app.get("/")
def root():

    return {
        "message": "F.R.I.D.A.Y API Online"
    }


@app.post("/users/{name}")
def create_user(name: str):

    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        (name,)
    )

    conn.commit()

    return {
        "status": "success",
        "user": name
    }


@app.get("/users")
def get_users():

    cursor.execute(
        "SELECT * FROM users"
    )

    users = cursor.fetchall()

    return {
        "users": users
    }

@app.post("/memory")
def save_memory(memory: Memory):

    cursor.execute(
        """
        INSERT INTO memories
        (user_id, memory_key, memory_value)
        VALUES (?, ?, ?)
        """,
        (
            memory.user_id,
            memory.key,
            memory.value
        )
    )

    conn.commit()

    return {
        "status": "saved"
    }

@app.get("/memory/{user_id}")
def get_memory(user_id: int):

    cursor.execute(
        """
        SELECT memory_key, memory_value
        FROM memories
        WHERE user_id = ?
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    result = {}

    for key, value in rows:
        result[key] = value

    return result