import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("REST_COUNTRIES_API_KEY")


def get_country(country_code):
    url = f'https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}'
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'}, params={"codes": country_code})
    return response

    