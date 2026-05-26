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

