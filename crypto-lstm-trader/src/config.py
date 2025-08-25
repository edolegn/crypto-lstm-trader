import os
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()

# Legge l'ambiente: TEST o MAIN (default MAIN)
BINANCE_ENV = os.getenv("BINANCE_ENV", "TEST").upper()

if BINANCE_ENV == "TEST":
    API_KEY = os.getenv("TEST_API_KEY")
    API_SECRET = os.getenv("TEST_API_SECRET")
    BASE_URL = "https://testnet.binance.vision"  # Spot testnet
else:
    API_KEY = os.getenv("MAIN_API_KEY")
    API_SECRET = os.getenv("MAIN_API_SECRET")
    BASE_URL = "https://api.binance.com"  # Spot mainnet

# Controllo validità
if API_KEY is None or API_SECRET is None:
    raise ValueError(f"Chiavi API mancanti per l'ambiente {BINANCE_ENV}. "
                     "Verifica il file .env.")