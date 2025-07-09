from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Ping": "API is running!"}