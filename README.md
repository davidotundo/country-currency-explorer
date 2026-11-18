# Currency & Country Explorer 🌍💱

A Python command-line application that retrieves country information and currency exchange rates using external APIs.

The application allows users to enter a country code and instantly retrieve essential country details, view selected exchange rates, and save the results in a JSON file.

## 🚀 Features

- **Country Information:** Retrieves country name, capital, population, and official currency.
- **Currency Exchange Rates:** Retrieves exchange rates for selected international currencies.
- **API Integration:** Combines data from two external APIs.
- **Error Handling:** Handles HTTP errors, invalid country codes, and API-specific errors.
- **JSON Export:** Saves retrieved country information and exchange rates in structured JSON files.
- **Command-Line Interface:** Provides a simple and user-friendly terminal experience.

## 🛠️ Technologies Used

- Python 3
- Requests
- JSON
- Python-dotenv
- REST Countries API
- ExchangeRate-API

## 📁 Project Structure

```text
currency_country_explorer/
│
├── main.py
├── country.py
├── currency.py
├── display.py
├── reports/
│
├── .env
├── .gitignore
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd currency_country_explorer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API credentials

Create a `.env` file in the project root and add your ExchangeRate-API key:

```env
EXCHANGE_RATE_API_KEY=your_api_key
REST_COUNTRIES_API_KEY =your_ap_key
```

Obtain an API key from [ExchangeRate-API](https://www.exchangerate-api.com/).
Obtain an API key from [RESTCOUNTRIES-API](https://restcountries.com/api-keys).

### 6. Run the application

```bash
python main.py
```

## 💻 Usage

When you run the application, you will be prompted to enter a two-letter country code.

Example:

```text
========================================
       CURRENCY & COUNTRY EXPLORER
========================================

Enter country code: KE
```

Supported examples:

| Country | Country Code |
|---|---|
| Kenya | KE |
| Uganda | UG |
| Tanzania | TZ |
| Rwanda | RW |
| South Africa | ZA |

The application retrieves the country's information and displays selected exchange rates.

## 📊 Sample Output

```text
========================================
          COUNTRY INFORMATION
========================================
Country       : Kenya
Capital       : Nairobi
Population    : 56,000,000
Currency      : KES

========================================
             EXCHANGE RATES
========================================
1 KES = 0.0077 USD (US Dollar)
1 KES = 0.0067 EUR (Euro)
1 KES = 0.0058 GBP (British Pound)
```

*Exchange rates shown are illustrative.*

## 💾 JSON Data Export

The application automatically saves the retrieved information in a JSON file.

Example filename:

```text
ke_country_report.json
```

The file contains:

- Country information
- Base currency
- Selected exchange rates

This allows users to access and reuse previously retrieved data without manually copying the results.

## 🛡️ Error Handling

The application includes handling for:

- Invalid country codes
- Empty user input
- Invalid country code formats
- Unauthorized API requests (401)
- Forbidden requests (403)
- Resource not found (404)
- API rate limits (429)
- Server errors (500 and above)
- API-specific error responses

## 🎯 Project Objectives

This project demonstrates practical Python development skills, including:

- Working with external REST APIs.
- Sending HTTP requests and processing JSON responses.
- Using Python dictionaries to extract nested data.
- Handling errors and validating user input.
- Organising code into reusable modules and functions.
- Reading environment variables for API credentials.
- Saving structured data to JSON files.
- Building command-line applications.

## 🔮 Future Improvements

- Allow users to compare multiple currencies.
- Add historical exchange rate comparisons.
- Allow users to retrieve previously saved reports.
- Add network timeout and connection error handling.
- Introduce automated tests using pytest.
- Improve the command-line interface with interactive menus.

## 👨‍💻 Author

**David Otundo**

Python Developer | Automation & AI Tools

Building practical applications that solve real-world problems.

---

*Developed as a practical Python API integration project.*