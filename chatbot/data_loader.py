import json
import os
from chatbot.structures import Intent

def load_intents(path="chatbot/data/intents.json"):
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if "intents" not in data:
        raise ValueError("O arquivo JSON não contém o campo 'intents'.")

    intents = [
        Intent(**intent)
        for intent in data["intents"]
    ]

    return intents
