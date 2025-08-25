import pandas as pd
import ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Aggiunge indicatori tecnici a un DataFrame OHLCV."""
    df = df.copy()
    
    # Indicatori di tendenza
    df["EMA20"] = ta.trend.EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    
    # Momentum
    rsi = ta.momentum.RSIIndicator(df["close"], window=14)
    df["RSI"] = rsi.rsi()
    
    # Volatilità
    bb = ta.volatility.BollingerBands(df["close"], window=20, window_dev=2)
    df["BB_High"] = bb.bollinger_hband()
    df["BB_Low"] = bb.bollinger_lband()
    df["BB_Width"] = df["BB_High"] - df["BB_Low"]
    
    # Volume
    df["OBV"] = ta.volume.OnBalanceVolumeIndicator(df["close"], df["volume"]).on_balance_volume()
    
    return df