from fastapi import FastAPI
import requests

app = FastAPI()

USPACY_WEBHOOK_URL = "https://hoper-trade.uspacy.ua/company/v1/incoming_webhooks/run/w92DJXqk5Ws8Gqyo8MozUXlpsqXLMBZH"

@app.get("/get_clients")
def get_clients():
    response = requests.get(USPACY_WEBHOOK_URL)
    return response.json()

@app.post("/add_client")
def add_client(client_id: int, name: str, status: str):
    payload = {"client_id": client_id, "name": name, "status": status}
    headers = {"Content-Type": "application/json"}
    response = requests.post(USPACY_WEBHOOK_URL, json=payload, headers=headers)
    return response.json()
