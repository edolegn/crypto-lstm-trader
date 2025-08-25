# Crypto Trading LSTM Project

Questo progetto scarica dati da Binance, calcola indicatori tecnici e prepara i dati per un modello LSTM.

## Struttura del progetto
- `data/raw/` – dati grezzi scaricati
- `data/processed/` – dati puliti e arricchiti con indicatori
- `src/config.py` – gestione delle chiavi API tramite `.env`
- `src/data_collection.py` – scarico dati e salvataggio su file
- `src/indicators.py` – funzioni per calcolare indicatori tecnici
- `src/utils.py` – funzioni di supporto
- `notebooks/EDA.ipynb` – esplorazione dati

## Setup
```bash
chmod +x setup_environment.sh
./setup_environment.sh