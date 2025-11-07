from chatbot.brain import get_response, get_intents
from chatbot.utils import log_message

def main():

    print("🤖 Chatbot iniciado! (digite 'sair' para encerrar)\n")

    while True:

        user_input = input("Você: ").strip()

        if get_intents(user_input) == "despedida":

            answer = get_response(user_input)
            print(f"Chatbot: {answer}")

            log_message("Usuário", user_input)
            log_message("Chatbot", answer)

            break

        log_message("Usuário", user_input)
        
        response = get_response(user_input)

        print(f"Chatbot: {response}")
        log_message("Chatbot", response)

if __name__ == "__main__":
    main()
