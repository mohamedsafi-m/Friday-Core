from fastapi import FastAPI
from database import cursor, conn

app = FastAPI(
    title="F.R.I.D.A.Y API",
    version="1.0.0"
)

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