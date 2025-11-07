from datetime import datetime

def log_message(sender: str, message: str):

    with open("chat_history.txt", "a", encoding="utf-8") as f:
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {sender}: {message}\n")