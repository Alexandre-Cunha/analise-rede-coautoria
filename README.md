# Análise de Rede de Coautoria de Pesquisadores

Trabalho Prático da disciplina **Algoritmos e Estruturas de Dados III (AEDS III)**, desenvolvido para análise de redes de coautoria acadêmica utilizando conceitos de Teoria dos Grafos.

---

# Sobre o Projeto

O sistema lê um arquivo contendo publicações acadêmicas e constrói uma **rede social ponderada de coautoria**, onde:

- Cada vértice representa um pesquisador.
- Cada aresta representa uma colaboração entre dois pesquisadores.
- O peso da aresta corresponde ao número de publicações realizadas em conjunto.

A partir dessa rede, o sistema realiza diversas análises estruturais e estatísticas para compreender os padrões de colaboração acadêmica.

---

# Funcionalidades

## Carregamento de Dados

- Leitura de arquivos `.txt`.
- Validação automática das publicações.
- Aceita publicações contendo entre 2 e 4 autores.
- Linhas inválidas são ignoradas e reportadas ao usuário.

## Construção do Grafo

- Geração automática dos pares de coautores.
- Criação de um grafo não direcionado e ponderado.
- Atualização automática dos pesos das arestas.

## Estatísticas da Rede

- Quantidade de pesquisadores.
- Quantidade de arestas distintas.
- Coeficiente de agrupamento médio.

## Métricas dos Pesquisadores

- Grau de cada pesquisador.
- Peso total das colaborações.

## Identificação de Pesquisadores Relevantes

- HUBs da rede (maior grau).
- Pesquisadores mais influentes (maior peso total).

## Análise de Distâncias

- Distância média da rede.
- Diâmetro da rede.

## Detecção de Comunidades

- Identificação de componentes conexos utilizando DFS (Depth First Search).

## Distribuição dos Graus

- Cálculo da frequência de cada grau.
- Geração automática de gráfico da distribuição de graus.

## Visualização da Rede

- Geração de imagem da rede de coautoria utilizando NetworkX.
- Tamanho dos nós proporcional ao grau do pesquisador.
- Espessura das arestas proporcional ao peso da colaboração.

## Relatório Automático

Geração automática de relatório em Markdown contendo:

- Estatísticas gerais;
- HUBs da rede;
- Pesquisadores mais influentes;
- Distância média;
- Diâmetro;
- Comunidades encontradas.

---

# Estrutura do Projeto

```text
.
├── main.py
├── functions.py
├── analise_rede.py
├── requirements.txt
│
├── dados/
│   ├── arquivo1.txt
│   ├── arquivo2.txt
│   └── arquivo3.txt
│
└── resultados/
    ├── relatorio_<rede>.md
    ├── distribuicao_graus_<rede>.png
    └── grafo_<rede>.png
```

---

# Formato do Arquivo de Entrada

Cada linha representa uma publicação acadêmica.

Os autores devem ser separados por ponto e vírgula:

```txt
Ana Clara; Joao Maria; Pedro Henrique
Carlos Eduardo; Pedro Henrique
Ana Clara; Joao Maria; Marcos Vinicius; Luiza Fernanda
Marcos Vinicius; Ana Clara
```

Cada publicação deve conter entre **2 e 4 autores**.

---

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/Alexandre-Cunha/analise-rede-coautoria.git
cd analise-rede-coautoria
```

## 2. Crie e ative um ambiente virtual

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Execute o programa

```bash
python main.py
```

---

# Menu de Funcionalidades

| Opção | Funcionalidade |
|---------|---------------|
| 1 | Carregar arquivo |
| 2 | Exibir grafo (lista de adjacência) |
| 3 | Exibir estatísticas |
| 4 | Exibir métricas dos pesquisadores |
| 5 | Encontrar HUBs da rede |
| 6 | Pesquisadores mais influentes |
| 7 | Distância média e diâmetro |
| 8 | Análise de comunidades |
| 9 | Distribuição dos graus |
| 10 | Gerar relatório completo |
| 0 | Sair |

---

# Arquivos Gerados

Ao executar a opção **10**, o sistema gera automaticamente:

```text
resultados/
├── relatorio_<rede>.md
├── distribuicao_graus_<rede>.png
└── grafo_<rede>.png
```

Esses arquivos são salvos utilizando o nome da rede analisada para evitar sobrescrita de resultados anteriores.

---

# Tecnologias Utilizadas

- Python 3
- Matplotlib
- NetworkX
- Estruturas de Dados
- Teoria dos Grafos
- Busca em Largura (BFS)
- Busca em Profundidade (DFS)

---

# Conceitos Aplicados

- Grafos ponderados
- Redes sociais
- Componentes conexos
- Análise de comunidades
- Métricas de centralidade
- Distribuição de graus
- Redes complexas
- Visualização de grafos

---

# Autor

**Alexandre Manoel Barreto da Cunha**

Trabalho desenvolvido para a disciplina **Algoritmos e Estruturas de Dados III (AEDS III)** – UFVJM.