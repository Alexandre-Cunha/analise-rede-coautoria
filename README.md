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

<<<<<<< HEAD
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
=======
### Métricas dos Pesquisadores
- Grau de cada pesquisador.
- Peso total das colaborações.

### Identificação de Pesquisadores Relevantes
- HUBs da rede (maior grau).
- Pesquisadores mais influentes (maior peso total).

### Análise de Distâncias
- Distância média entre pesquisadores.
- Diâmetro da rede.
- Utilização de Busca em Largura (BFS).

### Análise de Comunidades
- Identificação de componentes conexos.
- Utilização de Busca em Profundidade (DFS).

### Distribuição dos Graus
- Coleta dos graus dos vértices.
- Cálculo da frequência dos graus.
- Geração automática de gráfico da distribuição dos graus.

### Relatórios
- Geração automática de relatório em Markdown contendo os principais resultados da análise.

---

## Estrutura do Projeto

```text
analise-rede-coautoria/
│
├── dados/
│   └── arquivos de entrada (.txt)
│
├── resultados/
│   ├── relatórios gerados (.md)
│   └── gráficos gerados (.png)
│
├── main.py
├── functions.py
├── analise_rede.py
├── requirements.txt
└── README.md
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)
```

---

<<<<<<< HEAD
##  Formato do Arquivo de Entrada

Cada linha representa uma publicação e contém de 2 a 4 autores separados por ponto e vírgula.
=======
## Formato do Arquivo de Entrada

Cada linha representa uma publicação e deve conter entre 2 e 4 autores separados por ponto e vírgula.
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

Exemplo:

```txt
Ana Clara; Joao Maria; Pedro Henrique
Carlos Eduardo; Pedro Henrique
Ana Clara; Joao Maria; Marcos Vinicius; Luiza Fernanda
Marcos Vinicius; Ana Clara
```

---

<<<<<<< HEAD
##  Como Executar:

### 1. Clone o repositório
=======
## Como Executar

### 1. Clone o Repositório
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

```bash
git clone https://github.com/Alexandre-Cunha/analise-rede-coautoria.git
cd analise-rede-coautoria
```

<<<<<<< HEAD
### 2. Instale as dependências
=======
### 2. Crie um Ambiente Virtual (Opcional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
### 3. Execute o programa
=======
### 4. Adicione os Arquivos de Entrada

Coloque os arquivos `.txt` na pasta:

```text
dados/
```

### 5. Execute o Programa
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

```bash
python main.py
```

---

<<<<<<< HEAD
##  Menu de Funcionalidades
=======
## Menu de Funcionalidades
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

| Opção | Funcionalidade |
|---------|---------------|
| 1 | Carregar arquivo |
| 2 | Exibir grafo |
<<<<<<< HEAD
| 3 | Exibir estatísticas |
| 4 | Exibir métricas dos pesquisadores |
| 5 | Identificar hubs |
| 6 | Pesquisadores mais influentes |
| 7 | Distância média e diâmetro |
| 8 | Análise de comunidades |
| 9 | Distribuição de graus |
=======
| 3 | Estatísticas da rede |
| 4 | Métricas dos pesquisadores |
| 5 | Encontrar HUBs |
| 6 | Pesquisadores mais influentes |
| 7 | Distância média e diâmetro |
| 8 | Análise de comunidades |
| 9 | Distribuição dos graus |
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)
| 10 | Gerar relatório |
| 0 | Sair |

---

<<<<<<< HEAD
##  Tecnologias Utilizadas
=======
## Arquivos Gerados

Os resultados produzidos pelo sistema são armazenados automaticamente na pasta:

```text
resultados/
```

Exemplos:

```text
resultados/
├── relatorio_publicacoes.md
├── relatorio_rede_teste.md
├── distribuicao_graus_publicacoes.png
└── distribuicao_graus_rede_teste.png
```

---

## Tecnologias Utilizadas
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)

- Python 3
- Matplotlib
- Estruturas de Dados
- Teoria dos Grafos
<<<<<<< HEAD
=======
- Grafos Ponderados
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)
- Busca em Largura (BFS)
- Busca em Profundidade (DFS)

---

<<<<<<< HEAD
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
=======
## Conceitos Aplicados

Este projeto aplica conceitos estudados em:

- Teoria dos Grafos
- Redes Sociais
- Redes Complexas
- Análise de Colaboração Acadêmica
- Componentes Conexos
- Métricas de Centralidade
- Análise de Distâncias
- Visualização de Dados

---

## Autor

**Alexandre Manoel Barreto da Cunha**

Desenvolvido para a disciplina **Algoritmos e Estruturas de Dados III (AEDS III)** da UFVJM.
>>>>>>> 439ffc5 (feat: reorganizar estrutura do projeto)
