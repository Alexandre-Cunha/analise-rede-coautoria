import os

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

#Função para limpar o terminal, ela verifica qual S.O o usuário está utilizando e usa o comando do S.O correspondente. 
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

'''função que exibe um menu para o usuáro com opções de funcionalidades do programa'''
def menu():
    print("\n ======== MENU ========")
    print("1. Carregar arquivo de publicações")
    print("2. Exibir Grafo")
    print("3. Estatísticas")
    print("4. Exibir Métricas dos Pesquisadores")
    print("5. Encontrar HUBs da rede")
    print("6. Pesquisadores mais Influentes")
    print("0. Sair")