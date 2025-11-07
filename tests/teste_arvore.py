from chatbot.structures import Node, insert, inorder, search

def main():
    
    root = None

    root = insert(root, 5, "cinco")
    root = insert(root, 2, "dois")
    root = insert(root, 8, "oito")
    root = insert(root, 1, "um")
    root = insert(root, 3, "três")

    print("Percurso em-ordem da árvore:")
    inorder(root)

    key_to_search = 3
    result = search(root, key_to_search)

    if result:
        print(f"\nBusca: chave {key_to_search} → valor encontrado: {result}")
    else:
        print(f"\nBusca: chave {key_to_search} não encontrada.")

if __name__ == "__main__":
    main()
