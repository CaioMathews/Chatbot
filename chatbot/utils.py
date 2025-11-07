from datetime import datetime
from chatbot.structures import ChatHistory
from chatbot.structures import find_node

chat_history = ChatHistory()

def log_message(sender: str, message: str):
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_history.add_message(timestamp, f"{sender}: {message}")

def show_history():
    
    print("\n===== Histórico do Chat =====")
    chat_history.print_history()
    print("=============================\n")

def find_message(timestamp: str):

    return chat_history.find_node(timestamp)
