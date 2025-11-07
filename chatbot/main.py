from chatbot.brain import get_response
from chatbot.brain import get_intents
from chatbot.utils import log_message

def main():

    print("🤖 Chatbot iniciado! (digite 'sair' para encerrar)\n")

    while True:

        user_input = input("Você: ").strip()

        if get_intents(user_input) == "despedida":

            awnser = get_response(user_input)
            print(f"Chatbot: {awnser}")

            log_message("Usuário", user_input)
            log_message("Chatbot", awnser)

            break

        log_message("Usuário", user_input)

        response = get_response(user_input)

        print(f"Chatbot: {response}")
        log_message("Chatbot", response)

if __name__ == "__main__":
    main()
