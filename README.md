# 🚀 Smart Financial Data Pipeline

An automated industry-level ETL (Extract, Transform, Load) pipeline designed to fetch real-time cryptocurrency data, process it for analysis, and serve it through a professional API.

## 🌟 Features
- **Automated ETL:** Fetches the top 100 cryptocurrencies from the CoinGecko API.
- **Data Transformation:** Cleans and formats raw JSON data into structured Pandas DataFrames.
- **Persistent Storage:** Stores processed financial data in a MySQL database using SQLAlchemy.
- **RESTful API:** Serves live data via FastAPI with high performance.
- **Excel Export:** Built-in endpoint to download the entire dataset as a professional Excel report.
- **Smart Scheduler:** Background automation that keeps the database updated without manual intervention.

## 🏗️ Architecture
1. **Extractor:** Python `requests` library to interface with REST APIs.
2. **Transformer:** `Pandas` for data cleaning, type conversion, and normalization.
3. **Loader:** `SQLAlchemy` ORM for secure and efficient MySQL database operations.
4. **Backend:** `FastAPI` to provide a robust data access layer.
5. **Scheduler:** Python `schedule` module for 24/7 automation.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Analysis:** Pandas
- **Database:** MySQL
- **Web Framework:** FastAPI + Uvicorn
- **ORM:** SQLAlchemy
- **Excel Engine:** XlsxWriter / Openpyxl

## 🚀 Getting Started

### 1. Prerequisites
- MySQL Server installed and running.
- Python 3.10+ installed.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Uzair-hp/smart-pipeline.git
cd smart-pipeline

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=market_data
DB_PORT=3306
```

### 4. Running the Pipeline
```bash
# Start the Scheduler (Automated ETL)
python scheduler.py

# Start the API Server
uvicorn main:app --reload
```

## 📊 API Endpoints
- `GET /`: Health check.
- `GET /get-data`: Returns all stored cryptocurrency data in JSON format.
- `GET /export-excel`: Downloads a structured Excel report of the current market data.

## 🛡️ License
This project is open-source and available under the MIT License.

---
**Developed with ❤️ by [Uzair-hp](https://github.com/Uzair-hp)**
