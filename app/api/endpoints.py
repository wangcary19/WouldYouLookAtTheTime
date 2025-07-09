from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/time/now/{format}")
async def getCurrentTime(format: str):
    current_time = datetime.now()
    
# end-getCurrentTime()