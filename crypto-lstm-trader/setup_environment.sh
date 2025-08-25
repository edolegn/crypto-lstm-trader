#!/bin/bash

echo "Creazione virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Aggiornamento pip..."
pip install --upgrade pip

echo "Installazione dipendenze..."
pip install -r requirements.txt

echo "Environment pronto. Attivalo con:"
echo "source venv/bin/activate"