from chatbot.data_loader import load_intents
from chatbot.structures import Intent
import random

def preprocess(text):
    
    text = text.lower()

    for ch in [".", ",", "?", "!", ";", ":"]:
        text = text.replace(ch, "")

    return text.strip()

def text_similarity(a, b):

    a_words = set(preprocess(a).split())
    b_words = set(preprocess(b).split())

    if not a_words or not b_words:
        return 0.0
    
    intersection = len(a_words & b_words)
    union = len(a_words | b_words)

    return intersection / union

def find_best_intent(user_input: str, intents: list[Intent]):

    best_score = 0.0
    best_intent = None

    for intent in intents:

        for pattern in intent.patterns:  

            score = text_similarity(user_input, pattern)

            if score > best_score:
                best_score = score
                best_intent = intent

    return best_intent, best_score

def get_response(user_input: str):

    intents = load_intents("chatbot/data/intents.json")
    best_intent, score = find_best_intent(user_input, intents)

    if not best_intent or score < 0.2:
        return "Desculpe, não entendi o que você quis dizer."
    
    return random.choice(best_intent.responses) 

def get_intents(user_input: str):

    intents = load_intents("chatbot/data/intents.json")
    best_intent, score = find_best_intent(user_input, intents)

    if not best_intent or score < 0.2:
        return "Nenhuma intenção compatível!"
    
    return best_intent.tag
