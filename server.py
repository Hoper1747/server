import requests
from fastapi import FastAPI

app = FastAPI()

# Оновлений API-ендпоінт для отримання лідів з USPACY CRM
USPACY_API_URL = "https://hoper-trade.uspacy.ua/company/v1/incoming_webhooks/run/w92DJXqk5Ws8Gqyo8MozUXlpsqXLMBZH/crm/v1/entities/leads"

@app.get("/get_clients")
def get_clients():
    try:
        response = requests.get(USPACY_API_URL, timeout=10)  # Додаємо таймаут
        response.raise_for_status()  # Перевіряємо, чи немає 404 або 500 помилок
        return response.json()  # Якщо відповідь у форматі JSON, повертаємо її
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
