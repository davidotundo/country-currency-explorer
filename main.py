
"""
Currency & Country Explorer
============================

DESCRIPTION:
    A Python command-line application that retrieves country information
    and exchange rates using external APIs.

USAGE:
    1. Run the application using:
           python main.py

    2. Enter a two-letter ISO country code when prompted.
       Examples:
           KE - Kenya
           UG - Uganda
           TZ - Tanzania
           RW - Rwanda
           ZA - South Africa

    3. The application retrieves and displays:
           - Country name
           - Capital city
           - Population
           - Official currency
           - Selected exchange rates

    4. The application saves the retrieved information in a JSON file
       named after the country code.

OUTPUT:
    A country report in JSON format containing country information
    and selected exchange rates.

REQUIREMENTS:
    - Python 3
    - requests
    - python-dotenv
    - Valid API keys configured in the .env file

PROJECT MODULES:
    main.py       - Main application and user interface
    country.py    - Country information API requests
    currency.py   - Exchange rate API requests

AUTHOR:
    David Orare Otundo
"""


import json
from country import get_country
from currency import get_currency
from display import display_country_info
from display import display_exchange_rates

# =====================================
#           ERROR HANDLING
# =====================================

def handle_api_errors(response):

    errors = {
        400: "Bad request. Check your request.",
        401: "Unauthorized. Check your API key.",
        403: "Access forbidden.",
        404: "Resource not found.",
        429: "Too many requests. Try again later.",
        500: "Internal server error.",
        502: "Bad gateway.",
        503: "Service unavailable."
    }

    if response.status_code in errors:
        print(f"\nError {response.status_code}: {errors[response.status_code]}")
        return False

    if not response.ok:
        print(f"\nUnexpected HTTP error: {response.status_code}")
        return False

    return True


# =====================================
#          COUNTRY VALIDATION
# =====================================

def validate_country_code(country_code):

    if not country_code:
        print("\nPlease enter a country code.")
        return False

    if len(country_code) != 2 or not country_code.isalpha():
        print("\nInvalid input. Enter a two-letter country code.")
        return False

    return True

# =====================================
#          SAVING TO JSON
# =====================================

def save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nYour data has been saved successfully.")
        print(f"File: {filename}")

    except OSError as error:
        print(f"\nUnable to save file: {error}")

# =====================================
#             MAIN PROGRAM
# =====================================

def main():

    print("================================")
    print("  CURRENCY & COUNTRY EXPLORER   ")
    print("================================")

    country_code = input("Enter country code: ").strip().upper()

    # Validate country code format
    if not validate_country_code(country_code):
        return

    # =====================================
    #          COUNTRY INFORMATION
    # =====================================

    country_response = get_country(country_code)

    if not handle_api_errors(country_response):
        return

    country_results = country_response.json()['data']['objects']

    # Check if country exists
    if not country_results:
        print(f"\nCountry code '{country_code}' was not found.")
        return

    country_data = country_results[0]
    country_info = display_country_info(country_data)

    currency = country_info["currency"]


    # =====================================
    #             EXCHANGE RATES
    # =====================================

    currency_response = get_currency(currency)

    if not handle_api_errors(currency_response):
        return

    currency_json = currency_response.json()

    # Check API-specific errors
    if currency_json.get("result") == "error":
        print(f"\nCurrency API Error: {currency_json.get('error-type', 'Unknown error')}")
        return

    currency_data = currency_json['conversion_rates']

    selected_rates = display_exchange_rates(currency, currency_data)


    report = {
        "country_information": country_info,
        "exchange_rates": {
            "base_currency": currency,
            "rates": selected_rates
        }
    }

    filename = f"reports/{country_code.lower()}_country_report.json"
    save_to_file(report, filename)

    print("\n================================")
    print("       EXPLORATION COMPLETE     ")
    print("================================")

    
main()
