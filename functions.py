import os
from collections import deque
import analise_rede as ar

'''função que lê um arquivo de texto e extrai os autores de cada linha,  armazenando-os em uma lista de publicações.
Cada linha do arquivo é esperada estar no formato "autor1; autor2; autor3", onde os autores são separados por ponto e vírgula.
A função lida com possíveis erros, como o arquivo não ser encontrado ou outros erros de leitura,
e retorna uma lista de publicações ou uma mensagem de erro apropriada.'''

def carregar_arquivo(nome_arquivo):
    publicacoes = []
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as file:
            
            for linha in file:
                autores = [autor.strip() for autor in linha.split(";")]

            # validação se há entre 2 e 4 autores na publicação, caso contrário a linha é ignorada e uma mensagem de aviso é exibida'''
                if len(autores) < 2 or len(autores) > 4:

                    print(f"Linha ignorada: {linha.strip()}")
                    print("Uma publicação precisa ter entre 2 e 4 autores.\n")
                    continue

                publicacoes.append(autores)

        return publicacoes
    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []
  

'''função que recebe uma lista de autores de uma publicação e gera todos os pares possíveis de autores.
A função utiliza dois loops aninhados para iterar sobre a lista de autores e criar tuplas de pares,
garantindo que cada par seja único e não se repita.'''

def gerar_pares(publicacao):
    pares = []

    for i in range(len(publicacao)):
        for j in range(i + 1, len(publicacao)):
            pares.append((publicacao[i], publicacao[j]))

    return pares

'''Função responsável por construir um grafo não direcionado ponderado, onde o peso da aresta
entre dois pesquisadores é o número de publicações em que eles
aparecem juntos '''
def criar_grafo(publicacoes):
    grafo = {}

    for publicacao in publicacoes:
        pares = gerar_pares(publicacao)

        for autor1, autor2 in pares:

            # Cria o nó do autor1 naquela iteração caso ele não exista no grafo 
            if autor1 not in grafo:
                grafo[autor1] = {}
            # Cria o nó do autor2 naquela iteração caso ele não exista no grafo
            if autor2 not in grafo:
                grafo[autor2] = {}
            # Cria a aresta entre o autor1 e autor2 
            if autor2 not in grafo[autor1]:
                grafo[autor1][autor2] = 0
            # Cria a aresta entre o autor2 e autor1
            if autor1 not in grafo[autor2]:
                grafo[autor2][autor1] = 0

            # Como na Teoria dos Grafos os dois sentidos existem,
            # deve se adicionar o peso nos dois sentidos para que o Grafo seja consistente 
            grafo[autor1][autor2] += 1
            grafo[autor2][autor1] += 1 

    return grafo

# Função responsável por contar quantos pesquisadores existem no grafo, ela conta quantas chaves existem no dicionário.
def conta_pesquisadores(grafo):
    return len(grafo)

'''Funcão responsável por contar a quantidade de arestas do Grafo, como temos um grafo não direcionado temos que tratar as arestas
para evitar duplicatas, por isso usamos set() e tuple(sorted()).
'''
def conta_arestas(grafo):
    arestas = set() # O set cria uma coleção de valores únicos, ou seja não aceita duplicatas 

    for autor in grafo:
        for vizinho in grafo[autor]:
            aresta = tuple(sorted([autor, vizinho]))
            arestas.add(aresta)

    return len(arestas)

''' Função responsável por exibir as métricas Grau e Peso Total. O Grau é o número de vizinhos de cada nó do grafo 
e Peso Total é  a soma dos pesos das arestas conectadas a cada nó.'''
def calcular_metricas(grafo):
    metricas = {}

    for pesquisador in grafo:
        metricas[pesquisador] = {
            "grau": len(grafo[pesquisador]),
            "peso_total": sum(grafo[pesquisador].values()) 
        }

    return metricas

'''Função responsável por encontrar os HUBS da rede, HUBS são os nós com maior número de conexões diretas, 
ou seja HUBS são os nós com maior quantidade de arestas'''
def encontrar_hubs(metricas):
    maior_grau = max(dados["grau"] for dados in metricas.values())

    hubs = []

    for pesquisador, dados in metricas.items():
        if dados["grau"] == maior_grau:
            hubs.append(pesquisador)

    return hubs, maior_grau

'''Função responsável por encontrar os pesquisadores mais influentes, para um pesquisador ser o mais influente,
a soma do peso de suas arestas devem ser maior que a soma dos demais pesquisadoes'''
def encontrar_mais_influente(metricas):
    maior_peso = max(dados["peso_total"] for dados in metricas.values())

    influentes = []

    for pesquisador, dados in metricas.items():
        if dados["peso_total"] == maior_peso:
            influentes.append(pesquisador)

    return influentes, maior_peso

'''Função responsável por calcular o coeficiente de agrupamento médio da rede.
O cálculo é realizado pela média dos pesos das arestas do grafo, conforme
definido no enunciado do trabalho. Como o grafo é não direcionado, as arestas
são tratadas de forma única para evitar duplicidades. O valor retornado
representa a média de publicações por colaboração entre pesquisadores.'''
def coeficiente_agrupamento_medio(grafo):
    arestas = set() # O set cria uma coleção de valores únicos, ou seja não aceita duplicatas 
    soma_pesos = 0

    for autor in grafo:
        for vizinho, peso in grafo[autor].items():
            aresta = tuple(sorted([autor, vizinho]))

            if aresta not in arestas:
                arestas.add(aresta)
                soma_pesos += peso 

    return soma_pesos / len(arestas)

'''Função que realiza uma Busca em Largura (BFS) a partir de um pesquisador de origem.
A BFS percorre o grafo explorando primeiro os pesquisadores mais próximos da origem,
calculando a menor distância em número de arestas até cada pesquisador alcançável.

A função retorna um dicionário onde as chaves são os pesquisadores visitados
e os valores representam a distância mínima da origem até cada um deles.'''
def bfs(grafo, origem):
    fila = deque([origem])
    distancias = {
        origem: 0 
    }

    while fila:
        atual = fila.popleft()

        for vizinho in grafo[atual]:
            if  vizinho not in distancias:
                distancias[vizinho] = (distancias[atual] + 1)
                fila.append(vizinho)

    return distancias

'''Função responsável por calcular a distância média e o diâmetro da rede.
Para cada pesquisador da rede, é executada uma Busca em Largura (BFS) para
obter as menores distâncias até os demais pesquisadores.

A distância média é calculada pela média das menores distâncias entre todos
os pares de pesquisadores conectados. O diâmetro corresponde à maior dessas
distâncias, representando o maior menor caminho encontrado na rede.

Como a rede pode possuir componentes desconexos, pares de pesquisadores sem
caminho entre si são ignorados no cálculo.'''
def calcular_distancia_media_diametro(grafo):

    soma_distancias = 0
    quantidade_pares = 0
    diametro = 0

    pesquisadores = list(grafo.keys())

    for i in range(len(pesquisadores)):
        pesquisador = pesquisadores[i]
        distancias = bfs(grafo, pesquisador)

        for j in range(i + 1, len(pesquisadores)):
            outro = pesquisadores[j]
            if outro not in distancias:
                continue

            distancia = distancias[outro]
            soma_distancias += distancia
            quantidade_pares += 1

            if distancia > diametro:
                diametro = distancia

    distancia_media = soma_distancias / quantidade_pares

    return distancia_media, diametro

'''Função que realiza uma Busca em Profundidade (DFS) a partir de um pesquisador.
A DFS percorre recursivamente todos os pesquisadores alcançáveis a partir do
pesquisador inicial, visitando seus vizinhos e os vizinhos dos vizinhos até que
não existam mais vértices não visitados.

Os pesquisadores visitados são armazenados no conjunto 'visitados' para evitar
revisitas e ciclos, enquanto os integrantes da comunidade encontrada são
armazenados na lista 'comunidade'.'''
def dfs(grafo, pesquisador, visitados, comunidade):

    visitados.add(pesquisador)
    comunidade.append(pesquisador)

    for vizinho in grafo[pesquisador]:

        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, comunidade)

'''Função responsável por identificar as comunidades da rede de coautoria.
Uma comunidade é representada por um componente conexo do grafo, ou seja,
um grupo de pesquisadores que possuem algum caminho de colaboração entre si.

A função percorre todos os pesquisadores da rede e, para cada pesquisador
ainda não visitado, executa uma Busca em Profundidade (DFS) para encontrar
todos os membros de sua comunidade. Ao final, retorna uma lista contendo
todas as comunidades identificadas no grafo.'''
def encontrar_comunidades(grafo):
    visitados = set()
    comunidades = []

    for pesquisador in grafo:
        if pesquisador not in visitados:
            comunidade = []
            dfs(grafo, pesquisador, visitados, comunidade)
            comunidades.append(comunidade)

    return comunidades


#Função para limpar o terminal, ela verifica qual S.O o usuário está utilizando e usa o comando do S.O correspondente. 
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

'''Função responsável por gerar um relatório em formato Markdown
com as principais informações e métricas da rede de coautoria,
como estatísticas gerais, HUBs, pesquisadores mais influentes
e comunidades encontradas.'''
def gerar_relatorio_md(grafo, metricas, nome_rede):

    nome_arquivo = (f"resultados/relatorio_{nome_rede}.md")

    hubs, grau_hub = encontrar_hubs(metricas)
    influentes, peso_influente = encontrar_mais_influente(metricas)

    distancia_media, diametro = calcular_distancia_media_diametro(grafo)

    comunidades = encontrar_comunidades(grafo)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        arquivo.write("# Relatório de Análise da Rede de Coautoria\n\n")

        arquivo.write("## Estatísticas Gerais\n\n")

        arquivo.write(f"- **Pesquisadores:** {conta_pesquisadores(grafo)}\n")
        arquivo.write(f"- **Arestas Distintas:** {conta_arestas(grafo)}\n")
        arquivo.write(
            f"- **Coeficiente de Agrupamento Médio:** "
            f"{coeficiente_agrupamento_medio(grafo):.2f}\n\n"
        )

        arquivo.write("## Distâncias na Rede\n\n")

        arquivo.write(f"- **Distância Média:** {distancia_media:.2f}\n")
        arquivo.write(f"- **Diâmetro:** {diametro}\n\n")

        arquivo.write("## HUBs da Rede\n\n")

        for hub in hubs:
            arquivo.write(f"- {hub}\n")

        arquivo.write(f"\n**Maior grau encontrado:** {grau_hub}\n\n")

        arquivo.write("## Pesquisadores Mais Influentes\n\n")

        for pesquisador in influentes:
            arquivo.write(f"- {pesquisador}\n")

        arquivo.write(f"\n**Peso total:** {peso_influente}\n\n")

        arquivo.write("## Comunidades Encontradas\n\n")

        for i, comunidade in enumerate(comunidades, start=1):

            arquivo.write(
                f"### Comunidade {i} "
                f"({len(comunidade)} pesquisadores)\n\n"
            )

            for pesquisador in sorted(comunidade):
                arquivo.write(f"- {pesquisador}\n")

            arquivo.write("\n")

    print("\nRelatório gerado com sucesso!")
    print(f"Arquivo salvo como {nome_arquivo}")

'''função que exibe um menu para o usuáro com opções de funcionalidades do programa'''
def menu():
    print("\n ======== MENU ========")
    print("1. Carregar arquivo de publicações")
    print("2. Exibir Grafo")
    print("3. Estatísticas")
    print("4. Exibir Métricas dos Pesquisadores")
    print("5. Encontrar HUBs da rede")
    print("6. Pesquisadores mais Influentes")
    print("7. Distância Média e Diâmetro")
    print("8. Análise de Comunidades")
    print("9. Análise da Distribuição dos Graus e Gráfico")
    print("10. Gerar Relátorio")
    print("0. Sair")