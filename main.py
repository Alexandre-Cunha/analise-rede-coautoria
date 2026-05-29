from functions import menu, carregar_arquivo, gerar_pares, criar_grafo, limpar_terminal, conta_pesquisadores, conta_arestas


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try: 
            nome_arquivo = input("Digite o nome do arquivo: ")
            publicacoes = carregar_arquivo(nome_arquivo)
            print("\nArquivo carregado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    elif opcao == "2":
        try:
            for publicacao in publicacoes:
                pares = gerar_pares(publicacao)
            print("\nPares de autores gerados com sucesso.")
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    elif opcao == "3":
        grafo = criar_grafo(publicacoes)
        for autor in grafo:
            print(f"\n {autor}")
            for vizinho, peso in grafo[autor].items():
                print(f"   └── {vizinho} | peso: {peso}")

    elif opcao == "4":
        grafo = criar_grafo(publicacoes)
        print(f"\nExistem {conta_pesquisadores(grafo)} pesquisadores na rede.")

    elif opcao == "5":
        grafo = criar_grafo(publicacoes)
        print(f"\nExistem {conta_arestas(grafo)} arestas distintas na rede.")

    elif opcao == "0":
        print("Saindo...")
        limpar_terminal()
        exit()
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()