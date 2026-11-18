# =====================================
#          DISPLAY FUNCTIONS
# =====================================

def display_country_info(country_data):

    name = country_data['names']['common']
    capital = country_data['capitals'][0]['name']
    population = country_data['population']
    currency = country_data['currencies'][0]['code']

    print("\n" + "=" * 40)
    print("          COUNTRY INFORMATION")
    print("=" * 40)

    print(f"Country       : {name}")
    print(f"Capital       : {capital}")
    print(f"Population    : {population:,}")
    print(f"Currency      : {currency}")

    return {
        "country": name,
        "capital": capital,
        "population": population,
        "currency": currency
    }


def display_exchange_rates(currency, currency_data):

    selected_currencies = {
        "USD": "US Dollar",
        "EUR": "Euro",
        "GBP": "British Pound",
        "UGX": "Ugandan Shilling",
        "TZS": "Tanzanian Shilling",
        "RWF": "Rwandan Franc",
        "ZAR": "South African Rand"
    }

    print("\n" + "=" * 40)
    print("             EXCHANGE RATES")
    print("=" * 40)

    selected_rates = {}

    for code, currency_name in selected_currencies.items():

        rate = currency_data.get(code)

        if rate is not None:
            selected_rates[code] = rate

            print(f"1 {currency} = {rate:.4f} {code} ({currency_name})")

        else:
            print(f"{code}: Exchange rate unavailable.")

    return selected_rates

