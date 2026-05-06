from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def get_users():
    return [
        {"name": "Sowmya", "age": 22},
        {"name": "Ravi", "age": 20}
    ]