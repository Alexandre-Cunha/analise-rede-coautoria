import matplotlib.pyplot as plt

'''Função responsável por calcular a distribuição dos graus da rede.
Ela conta quantos pesquisadores possuem cada valor de grau e
retorna um dicionário contendo a frequência de cada grau.'''
def distribuicao_graus(grafo):

    frequencias = {}

    for pesquisador in grafo:

        grau = len(grafo[pesquisador])

        if grau not in frequencias:
            frequencias[grau] = 0

        frequencias[grau] += 1

    return frequencias

'''Função responsável por gerar um gráfico de barras da distribuição
dos graus da rede. O eixo x representa os graus dos pesquisadores
e o eixo y representa a frequência de cada grau.'''
def plotar_distribuicao_graus(frequencias):

    graus = sorted(frequencias.keys())
    valores = [frequencias[g] for g in graus]

    plt.figure(figsize=(8,5))
    plt.bar(graus, valores)

    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Graus")

    plt.savefig(
        "distribuicao_graus.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Gráfico salvo em distribuicao_graus.png")