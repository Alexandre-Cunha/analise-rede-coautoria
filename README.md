# Análise de Rede de Coautoria de Pesquisadores

Trabalho Prático da disciplina **AEDS III**, desenvolvido para análise de redes de coautoria acadêmica utilizando conceitos de Teoria dos Grafos.

##  Sobre o Projeto

O sistema lê um arquivo contendo publicações acadêmicas e constrói uma **rede social ponderada de coautoria**, onde:

- Cada vértice representa um pesquisador.
- Cada aresta representa uma colaboração entre dois pesquisadores.
- O peso da aresta corresponde ao número de publicações realizadas em conjunto.

A partir dessa rede, o sistema calcula diversas métricas e estatísticas para análise da colaboração acadêmica.

---

##  Funcionalidades

###  Carregamento de Dados
- Leitura de arquivos `.txt` contendo publicações.
- Validação de linhas com 2 a 4 autores.

###  Construção do Grafo
- Geração automática de todos os pares de coautores.
- Criação de um grafo não direcionado ponderado.

###  Estatísticas da Rede
- Quantidade de pesquisadores.
- Quantidade de arestas distintas.
- Coeficiente de agrupamento médio.

###  Métricas por Pesquisador
- Grau (número de colaboradores diretos).
- Peso total das colaborações.

###  Identificação de Pesquisadores Relevantes
- Hubs da rede (maior grau).
- Pesquisadores com maior peso total de colaboração.

###  Análise de Distâncias
- Distância média entre pesquisadores.
- Diâmetro da rede.

###  Detecção de Comunidades
- Identificação de componentes conexos utilizando Busca em Profundidade (DFS).

###  Distribuição dos Graus
- Cálculo da frequência dos graus.
- Geração automática de gráfico da distribuição.

###  Relatório
- Geração de relatório contendo os principais resultados da análise.

---

##  Estrutura do Projeto

```text
.
├── main.py                 # Menu principal da aplicação
├── functions.py            # Funções de manipulação e análise do grafo
├── analise_rede.py         # Distribuição de graus e geração de gráficos
├── requirements.txt        # Dependências do projeto
├── arquivo3.txt            # Exemplo de entrada
└── distribuicao_graus.png  # Gráfico gerado pelo sistema
```

---

##  Formato do Arquivo de Entrada

Cada linha representa uma publicação e contém de 2 a 4 autores separados por ponto e vírgula.

Exemplo:

```txt
Ana Clara; Joao Maria; Pedro Henrique
Carlos Eduardo; Pedro Henrique
Ana Clara; Joao Maria; Marcos Vinicius; Luiza Fernanda
Marcos Vinicius; Ana Clara
```

---

##  Como Executar:

### 1. Clone o repositório

```bash
git clone https://github.com/Alexandre-Cunha/analise-rede-coautoria.git
cd analise-rede-coautoria
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o programa

```bash
python main.py
```

---

##  Menu de Funcionalidades

| Opção | Funcionalidade |
|---------|---------------|
| 1 | Carregar arquivo |
| 2 | Exibir grafo |
| 3 | Exibir estatísticas |
| 4 | Exibir métricas dos pesquisadores |
| 5 | Identificar hubs |
| 6 | Pesquisadores mais influentes |
| 7 | Distância média e diâmetro |
| 8 | Análise de comunidades |
| 9 | Distribuição de graus |
| 10 | Gerar relatório |
| 0 | Sair |

---

##  Tecnologias Utilizadas

- Python 3
- Matplotlib
- Estruturas de Dados
- Teoria dos Grafos
- Busca em Largura (BFS)
- Busca em Profundidade (DFS)

---

##  Objetivo Acadêmico

Este projeto foi desenvolvido para aplicar conceitos de:

- Grafos ponderados
- Redes sociais
- Métricas de centralidade
- Componentes conexos
- Análise de redes complexas
- Visualização de dados

---

##  Autor

**Alexandre Manoel Barreto da Cunha**

Trabalho desenvolvido para a disciplina **Algoritmos e Estruturas de Dados III (AEDS III)** – UFVJM.
