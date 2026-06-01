from functions import menu, carregar_arquivo, criar_grafo, limpar_terminal, conta_pesquisadores, conta_arestas, calcular_metricas

publicacoes = None
grafo = None

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo: ")
            publicacoes = carregar_arquivo(nome_arquivo)

            if publicacoes:
                grafo = criar_grafo(publicacoes)
                print("\nArquivo carregado com sucesso!")
            else:
                print("\nNenhuma publicação foi carregada.")

    elif opcao == "2":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue

        for autor in sorted(grafo):            
            print(f"\n {autor}")
            for vizinho, peso in sorted(grafo[autor].items()):
                print(f"   └── {vizinho} | peso: {peso}")

    elif opcao == "3":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue
        
        print("\n ===== ESTATÍSTICAS =====")
        print(f"Pesquisadores: {conta_pesquisadores(grafo)}")
        print(f"Arestas Distintas: {conta_arestas(grafo)}")

    elif opcao == "4":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue

        metricas = calcular_metricas(grafo)
        print("\n ===== MÉTRICAS =====")
        for pesquisador, dados in sorted(metricas.items(), key=lambda item: item[1]["grau"],reverse=True):
            print(f'\n{pesquisador}')
            print(f"Grau: {dados['grau']}")
            print(f"Peso Total:  {dados['peso_total']}\n")
        
    elif opcao == "0":
        print("Saindo...")
        limpar_terminal()
        exit()
    else:
        print("Opção inválida. Tente novamente.")
