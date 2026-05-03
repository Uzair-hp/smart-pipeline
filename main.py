from fastapi import FastAPI
import pandas as pd
from database import engine
from fastapi.responses import StreamingResponse
import io


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Data Pipeline API is running"}

@app.get("/get-data")
def get_data():
    # Use pandas to read the table directly from the database engine
    df = pd.read_sql("SELECT * FROM coin_data", engine)
    return df.to_dict(orient='records')

@app.get("/export-excel")
def export_excel():
    df = pd.read_sql("SELECT * FROM coin_data", engine)
    
    # Create an in-memory bytes buffer
    output = io.BytesIO()
    
    # Write the DataFrame to the buffer as an Excel file
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='CoinData')
    
    # Seek to the beginning of the stream
    output.seek(0)
    
    # Return the buffer as a streaming response with appropriate headers
    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={"Content-Disposition": "attachment; filename=coin_data.xlsx"})