from chatbot.structures import Node, insert_node, print_inorder, find_node

def main():
    
    root = None

    print("Inserindo elementos na árvore AVL:\n")

    root = insert_node(root, 5, "cinco")
    root = insert_node(root, 2, "dois")
    root = insert_node(root, 8, "oito")
    root = insert_node(root, 1, "um")
    root = insert_node(root, 3, "três")

    print("\nPercurso em ordem (inorder):")
    print_inorder(root)

    print("\n🔎 Teste de busca:")

    for key in [3, 4, 8]:

        result = find_node(root, key)

        if result:
            print(f"  Chave {key} → valor encontrado: {result}")
        else:
            print(f"  Chave {key} não encontrada.")

if __name__ == "__main__":
    main()
