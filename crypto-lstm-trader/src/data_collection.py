import pandas as pd
from binance.client import Client
from src.config import API_KEY, API_SECRET, BASE_URL
from src.utils import ensure_dir
from src.indicators import add_indicators


DATA_RAW_PATH = "data/raw/binance_data.csv"
DATA_PROCESSED_PATH = "data/processed/binance_data_with_indicators.csv"

def download_binance_data(symbol="BTCEUR", interval="1h", limit=1000):

    print(f"Sto usando l'ambiente Binance: {BASE_URL}")
    print(f"Chiave pubblica: {API_KEY[:6]}...")  # non stampare tutta la chiave!
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.API_URL = BASE_URL
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    
    df = pd.DataFrame(klines, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    
    # Converte i campi numerici
    numeric_cols = ["open", "high", "low", "close", "volume"]
    df[numeric_cols] = df[numeric_cols].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    
    return df[["open_time", "open", "high", "low", "close", "volume"]]

if __name__ == "__main__":
    ensure_dir("data/raw")
    ensure_dir("data/processed")
    
    print("Scarico dati da Binance...")
    df = download_binance_data()
    df.to_csv(DATA_RAW_PATH, index=False)
    print(f"Dati grezzi salvati in {DATA_RAW_PATH}")
    
    print("Aggiungo indicatori tecnici...")
    df_ind = add_indicators(df)
    df_ind.to_csv(DATA_PROCESSED_PATH, index=False)
    print(f"Dati con indicatori salvati in {DATA_PROCESSED_PATH}")