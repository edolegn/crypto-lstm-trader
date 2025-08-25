import pandas as pd
import os
from datetime import datetime

def save_dataframe(df: pd.DataFrame, filename: str):
    """Salva un dataframe in formato CSV nella cartella data/processed."""
    path = f"data/processed/{filename}"
    df.to_csv(path, index=False)
    print(f"File salvato in: {path}")

def timestamp_to_str(ts: int) -> str:
    """Converte un timestamp Binance in stringa leggibile."""
    return datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%d %H:%M:%S')


def ensure_dir(path: str):
    """Crea la cartella se non esiste."""
    if not os.path.exists(path):
        os.makedirs(path)