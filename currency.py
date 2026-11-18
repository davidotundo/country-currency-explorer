import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGE_RATE_API_KEY")

def get_currency(currency_code):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency_code}"
    response = requests.get(url)
    return response
