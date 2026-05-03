import pandas as pd
import requests
from database import engine 

def fetch_coin_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def transform_data(data):
    df=pd.DataFrame(data)
    columns=['id','symbol','name','current_price','market_cap','last_updated']
    df=df[columns]
    
    df = df.rename(columns={'id': 'coin_id'})
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    
    return df

def load_data(df):
    df.to_sql('coin_data', con=engine, if_exists='replace', index=False)
    print("✅ Data loaded into the database successfully.")
    
    
if __name__ == "__main__":
    raw_data=fetch_coin_data()
    if raw_data:
        df=transform_data(raw_data)
        print("✅ Data fetched and transformed successfully." )
        
        load_data(df)
        