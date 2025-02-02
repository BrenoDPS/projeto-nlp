# Ford - Teste Técnico - Processamento de Linguagem Natural (NLP)

# Predição de Probabilidade de Recall

## Resumo

Esse repositório contém a resolução de um desafio técnico proposto para selecionar um conjunto de dados de reclamações de veículos do NHTSA e construir um modelo, preferencialmente baseado em embeddings (como Word2Vec, GloVe, FastText ou modelos de transformadores pré-treinados como BERT, RoBERTa, etc.), capaz de realizar uma tarefa de classificação ou regressão relevante extraída dos dados.
A tarefa escolhida foi de realizar um modelo baseado em predição de probabilidade de recalls analisando diferentes features, como "FIRE", "INJURED", "DEATHS" e "CRASH", em que cada um tinha um peso a ser considerado, como por exemplo, "CRASH" recebe peso 2 (acidente aumenta significativamente a severidade), "FIRE" recebe peso 3 (incêndio é crítico para segurança), "INJURED" recebe peso 1.5 (feridos indicam risco alto) e "DEATHS" recebe peso 3 (fatalidades são o indicador mais grave).

## Estrutura do Repositório

A estrutura do repositório foi organizada da seguinte forma:

```
projeto-nlp/
│
├── .github
│    └── workflows
│        └── ci.yml                   # Configuração para o GitHub Actions e CI/CD da aplicação
│
├── data/                              # Dados brutos e processados
│   ├── raw/                           # Dados brutos baixados do NHTSA
│   ├── processed/                     # Dados totalmente processados (prontos para modelagem)
│   └── interim/                       # Dados intermediários (ex: .csv estruturado)
│
├── docs/                              # Documentação a partir do app mkdocs
│   ├── my-project/
│   │   └── docs/
│   │        ├── index.md              # Documentação explicando Features e Passo a Passo do Projeto 
│   │        └── TesteNLP.md           # Documentação e relatório sobre a realização do Projeto que foi passado de antemão
│   │
│   └── mkdocs.yml                     # Arquivo ".yml" para rodar a documentação do projeto em localhost
│
├── notebooks/                         # Jupyter Notebooks para EDA e experimentação
│   └── 01_eda.ipynb                   # Análise exploratória de dados, Pré-processamento de texto e Treinamento do modelo
│   
│
├── src/                               # Código fonte principal
│   ├── data_processing.py             # Scripts para limpeza e pré-processamento
│   ├── filtrar_2014.py                # Script para filtrar o dataset original com dados 2010 a 2014 para apenas dados de 2014
│   ├── converter_txt_para_csv.py      # Script para converter os datasets em formato ".txt" para ".csv"
│   └── limpar_texto.py                # Script para tratamento de Strings com lematização e remoção de stopwords
│
├── logs/
│   └── merge_logs.log                 # Arquivo dump de logs especificados nos scripts Python
│
├── tests/                             # Testes de integração
│   ├── test_data_processing.py        # Testes para pré-processamento
│   └── conftest.py                    # Configurações e fixtures globais
│
├── Dockerfile                         # Arquivo Docker para conteinerização
├── requirements.txt                   # Dependências do projeto
├── Makefile                           # Automação de tarefas (ex.: instalar dependências, rodar testes)
├── README.md                          # Documentação do projeto
└── .gitignore                         # Ignorar arquivos desnecessários no Git
```


## Executando o Notebook

Para executar o notebook e reproduzir os resultados, siga estes passos:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/projeto-nlp.git
   cd projeto-nlp
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências necessárias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

5. **Execute a pipeline de scripts:**
      
   Execute os códigos "converter_txt_para_csv.py", em seguida "filtrar_2014.py", "mesclar_datasets.py" e "limpar_texto.py".

6. **Abra e execute o notebook:**

   Na interface do Jupyter, navegue até `notebooks/01_eda.ipynb` e execute todas as células para rodar o código e reproduzir a análise e os resultados.

## Descrição do Projeto

O notebook está estruturado em várias seções-chave:

1. **Carregamento e Exploração de Dados**: Carregamento do dataset e realização de exploração inicial e visualizações.
2. **Tratamento de Valores Nulos ou Faltantes**: Análise de valores nulos que podem enviesar o treinamento.
3. **Pré-processamento de Dados**: Limpeza dos dados, tratamento de valores ausentes e engenharia de features.
4. **Analisando a Target Feature**: Estudo da melhor manipulação das colunas para encontrar um target ideal.
5. **Treinamento do Modelo**: Treinamento de vários modelos de machine learning e avaliação de sua performance.

## Execução dos Testes

Para garantir a integridade do projeto, você pode executar os testes incluídos no repositório. Siga estes passos:

1. **Instale as dependências para testes:**

   ```bash
   pip install pytest
   ```

2. **Execute os testes:**

   ```bash
   pytest
   ```

Os testes irão automaticamente descobrir e rodar qualquer arquivo de teste no repositório, garantindo que as etapas de processamento de dados, treinamento e avaliação do modelo estejam funcionando corretamente.

---

Sinta-se à vontade para entrar em contato se tiver alguma dúvida ou precisar de mais assistência!