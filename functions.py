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
            if autor1 not in grafo[autor1]:
                grafo[autor2][autor1] = 0

            # Como na Teoria dos Grafos os dois sentidos existem,
            # deve se adicionar o peso nos dois sentidos para que o Grafo seja consistente 
            grafo[autor1][autor2] += 1
            grafo[autor2][autor1] += 1 

    return grafo


#Função para limpar o terminal, ela verifica qual S.O o usuário está utilizando e usa o comando do S.O correspondente 
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")