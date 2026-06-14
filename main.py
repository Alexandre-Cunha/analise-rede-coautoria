import functions as fn

publicacoes = None
grafo = None
metricas = None

while True:
    fn.menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo: ")
            publicacoes = fn.carregar_arquivo(nome_arquivo)

            if publicacoes:
                grafo = fn.criar_grafo(publicacoes)
                metricas = fn.calcular_metricas(grafo)
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
        print(f"Pesquisadores: {fn.conta_pesquisadores(grafo)}")
        print(f"Arestas Distintas: {fn.conta_arestas(grafo)}")
        print(f"Coeficiente de Agrupamento Médio: {fn.coeficiente_agrupamento_medio(grafo):.2f}")

    elif opcao == "4":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue

        print("\n ===== MÉTRICAS =====")
        for pesquisador, dados in sorted(metricas.items(), key=lambda item: item[1]["grau"],reverse=True):
            print(f'\n{pesquisador}')
            print(f"Grau: {dados['grau']}")
            print(f"Peso Total:  {dados['peso_total']}\n")

    elif opcao == "5":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue

        hubs, grau = fn.encontrar_hubs(metricas)

        print("\n===== HUBS DA REDE =====")

        for i, hub in enumerate(hubs, start=1):
            print(f"{i}. {hub}")

        print(f"\nMaior grau encontrado: {grau}")
        
    elif opcao == "6":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue
        
        influentes, peso = fn.encontrar_mais_influente(metricas)

        print("\n===== PESQUISADORES MAIS INFLUENTES =====\n")

        for pesquisador in influentes:
            print(f'Pesquisador: {pesquisador}')
        print(f"\nPeso Total: {peso}")

    elif opcao == "7":
        if grafo is None:
            print("Carregue um arquivo primeiro.")
            continue
        
        dist_media, diametro = (fn.calcular_distancia_media_diametro(grafo))

        print("\n===== DISTÂNCIAS =====")
        print(f"Distância Média: {dist_media:.2f}")
        print(f"Diâmetro: {diametro}")
        

    elif opcao == "0":
        print("Saindo...")
        fn.limpar_terminal()
        exit()
    else:
        print("Opção inválida. Tente novamente.")
