from chatbot.brain import get_response

def main():

    print("🤖 Chatbot iniciado! (digite 'sair' para encerrar)\n")

    while True:

        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:

            print("Chatbot: Até logo! 👋")
            break

        response = get_response(user_input)
        
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()
