import matplotlib.pyplot as plt
import networkx as nx
import os

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
def plotar_distribuicao_graus(frequencias, nome_rede):

    nome_arquivo = (f"resultados/distribuicao_graus_{nome_rede}.png")

    graus = sorted(frequencias.keys())
    valores = [frequencias[g] for g in graus]

    plt.figure(figsize=(8,5))
    plt.bar(graus, valores)

    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.title("Distribuição dos Graus")

    plt.savefig(
        nome_arquivo,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"\nGráfico salvo em {nome_arquivo}")

'''Função responsável por gerar uma imagem da rede de coautoria.
Os nós representam pesquisadores e as arestas representam
colaborações entre eles.'''
def gerar_imagem_grafo(grafo, nome_rede):

    os.makedirs("resultados", exist_ok=True)
    nome_arquivo = f"resultados/grafo_{nome_rede}.png"

    G = nx.Graph()

    for autor in grafo:

        for vizinho, peso in grafo[autor].items():

            G.add_edge(

                autor,

                vizinho,

                weight=peso

            )
            
    plt.figure(figsize=(14, 10))

    pos = nx.spring_layout(
        G,
        seed=42,
        k=1.2
    )

    node_sizes = [
        300 + (100 * G.degree(n))
        for n in G.nodes()
    ]

    node_colors = [
        G.degree(n)
        for n in G.nodes()
    ]

    edge_widths = [
        G[u][v]["weight"] * 0.5
        for u, v in G.edges()
    ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_sizes,
        node_color=node_colors,
        cmap=plt.cm.viridis,
        alpha=0.9
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=edge_widths,
        edge_color="gray",
        alpha=0.4
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=8,
        font_weight="bold"
    )

    plt.title(
        f"Grafo - Rede de Co-autoria",
        fontsize=16
    )

    plt.savefig(
    nome_arquivo,
    dpi=300,
    bbox_inches="tight"
)

    plt.axis("off")
    plt.tight_layout()
    plt.close()

    print(f"\nGrafo salvo em {nome_arquivo}")