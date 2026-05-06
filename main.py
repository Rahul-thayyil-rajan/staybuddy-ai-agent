from fastapi import FastAPI
from app.agents import smart_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Hotel Agent Running"}

@app.get("/agent")
def run(query: str):
    return smart_agent(query)