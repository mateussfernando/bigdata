# ETL de Universidades - Big Data

Um projeto de **Extract, Transform, Load (ETL)** que extrai dados de universidades de diferentes países da API HipoLabs e carrega os dados em bancos de dados SQLite e MongoDB.

## 📋 Descrição

Este projeto implementa um pipeline ETL automatizado que:

- **Extrai** dados de universidades de uma API pública (`universities.hipolabs.com`)
- **Carrega** os dados em dois tipos de banco de dados:
  - **SQLite**: para armazenamento local estruturado
  - **MongoDB Atlas**: para armazenamento em nuvem (NoSQL)
- **Orquestra** o fluxo com **Prefect** para execução agendada diária

## 🚀 Funcionalidades

- ✅ Extração de dados de universidades por país
- ✅ Carregamento em SQLite local
- ✅ Carregamento em MongoDB Atlas
- ✅ Agendamento automático com Prefect (executado diariamente às 8h UTC)
- ✅ Tratamento de erros com retry automático
- ✅ Logging detalhado de operações

## 📁 Estrutura do Projeto

```
bigdata/
├── main.py                      # Script principal para execução manual
├── orchestrate_prefect.py       # Orquestração com Prefect (agendamento)
├── teste.py                     # Scripts de teste
├── requirements.txt             # Dependências do projeto
├── README.md                    # Este arquivo
└── src/
    ├── extract.py              # Classe de extração de dados
    └── load.py                 # Classe de carregamento (SQLite e MongoDB)
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **requests**: Para requisições HTTP à API
- **SQLite**: Banco de dados local
- **PyMongo**: Driver para MongoDB
- **Prefect**: Orquestração e agendamento de workflows
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **pandas**: Manipulação de dados
- **black**: Formatação de código

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/mateussfernando/bigdata.git
cd bigdata
```

### 2. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_URI=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/?retryWrites=true&w=majority
```

## 💻 Uso

### Execução Manual

Para executar o ETL uma única vez:

```bash
python main.py
```

### Execução com Orquestração Prefect

Para ativar o agendamento automático (execução diária às 8h UTC):

```bash
python orchestrate_prefect.py
```

Isso iniciará a **Prefect Server** e agendará o fluxo para executar automaticamente todos os dias.

### Monitoramento

Acesse a interface do Prefect em `http://localhost:4200` para monitorar as execuções do fluxo.

## 📊 Dados Extraídos

O projeto extrai as seguintes informações sobre universidades:

| Campo            | Descrição                   |
| ---------------- | --------------------------- |
| `name`           | Nome da universidade        |
| `country`        | País da universidade        |
| `state-province` | Estado/Província            |
| `web_pages`      | Páginas web da universidade |
| `domains`        | Domínios da universidade    |

## 📝 Exemplos

### Extract

```python
from src.extract import Extract

extractor = Extract()
universities = extractor.extract_data("Brazil")
print(f"Extraídas {len(universities)} universidades do Brasil")
```

### Load - SQLite

```python
from src.load import Load

loader = Load()
loader.load_data_sqlite(universities, "tabela_brazil")
```

### Load - MongoDB

```python
from src.load import Load

loader = Load()
loader.load_data_atlas(universities, "universidades", "universidades_brazil")
```

## 🔄 Fluxo ETL com Prefect

O arquivo `orchestrate_prefect.py` define um fluxo Prefect que:

1. **Extrai** dados de universidades do Brasil
2. **Carrega** os dados no MongoDB Atlas
3. **Executa** automaticamente todos os dias às 8h (UTC)

```python
@flow(name="ETL Universities Prefect", log_prints=True)
def etl_universities_flow(country: str = "Brazil"):
    data = extract(country)
    load_data(data, "universidades", "universidades_brazil")
```

**Configuração de Agendamento:**

- **Cron**: `0 8 * * *` (todos os dias às 8h UTC)
- **Tags**: `["etl", "universities"]`

## 🐛 Troubleshooting

### Erro de conexão com MongoDB

- Verifique se a `MONGO_URI` está correta no arquivo `.env`
- Verifique se seu IP está permitido no MongoDB Atlas
- Verifique a conectividade de rede

### Erro de requisição à API

- Verifique a disponibilidade da API: `http://universities.hipolabs.com`
- Verifique a conectividade de rede
- O retry automático tentará até 3 vezes com aguardo de 10 segundos

### Prefect não está agendando

- Verifique se o Prefect Server está rodando em background
- Acesse `http://localhost:4200` para confirmar
- Verifique os logs do Prefect para mais detalhes

## 📚 API Utilizada

**URL**: `http://universities.hipolabs.com/search?country={country}`

**Exemplo de Resposta**:

```json
[
  {
    "name": "University of São Paulo",
    "country": "Brazil",
    "state-province": "São Paulo",
    "web_pages": ["http://www.usp.br/"],
    "domains": ["usp.br"]
  }
]
```

## 📄 Licença

Este projeto é de código aberto.

## 👨‍💻 Autor

**Mateus Fernando**

---
