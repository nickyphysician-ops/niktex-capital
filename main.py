import os
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Niktex Capital Public Cloud Engine")

class DepositRequest(BaseModel):
    phone_number: str
    amount: float

@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Niktex Front-End Configuration File Missing</h1>"

@app.post("/api/v1/payments/stk-push")
async def initiate_stk_push(request: DepositRequest):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return {
        'status': 'Success', 
        'message': f'Welcome to Niktex Capital Trading! Secure push request sent to {request.phone_number}.', 
        'ref_id': 'MP' + timestamp[8:] + 'NK'
    }
