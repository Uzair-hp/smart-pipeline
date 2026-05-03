import schedule
import time
from etl_job import fetch_coin_data, transform_data, load_data 

def run_etl_pipeline():
    print("Starting ETL pipeline...")
    
    try:
        raw_data = fetch_coin_data()
        if raw_data:
            df=transform_data(raw_data)
            load_data(df)
            print("ETL pipeline completed successfully.")
    except Exception as e:
        print(f"Error during ETL pipeline: {e}")
        
schedule.every(5).hours.do(run_etl_pipeline)

if __name__ == "__main__":
    print("Scheduler started. Running ETL pipeline every 5 hours.")
    run_etl_pipeline()  # Run immediately on startup
    while True:
        schedule.run_pending()
        time.sleep(1)