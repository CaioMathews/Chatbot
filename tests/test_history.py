from chatbot.structures import ChatHistory

def main():
    history = ChatHistory()

    history.add_message("Usuário", "Olá, bot!")
    history.add_message("Chatbot", "Olá, humano!")
    history.add_message("Usuário", "Como você está?")
    history.add_message("Chatbot", "Estou ótimo, obrigado!")

    print("\n Histórico completo (em ordem):")
    history.print_history()

    print("\n Busca pelo ID 2:")
    print(history.get_message(2))

if __name__ == "__main__":
    main()
