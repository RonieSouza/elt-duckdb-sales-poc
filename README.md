<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/40/DuckDB_logo.svg" alt="DuckDB Logo" width="150"/>
</p>
<p align="center">
  <b>Este projeto utiliza <a href="https://duckdb.org">DuckDB</a> motor principal de processamento analítico.</b><br/>
</p>

# ELT-DUCKDB-SALES-POC

PoC de ELT com Python e DuckDB em Docker, estruturada em camadas **Bronze**, **Silver** e **Gold**, com modelagem final em **Star Schema (Kimball)**. Foco em leveza, performance, simplicidade aproveitando recursos open source.

---

## 🚀 Sobre o Projeto

Este projeto é uma **prova de conceito (PoC)** desenvolvida para demonstrar um processo completo de **ELT local** com foco em:

- Estrutura por camadas: **Bronze**, **Silver**, **Gold**.
- Leveza e desempenho com **DuckDB**.
- Modelagem dimensional (Kimball) na camada Gold.
- Armazenamento local com **arquivos .parquet**.
- Execução rápida e portátil com **Docker**.
- Desenvolvimento orientado por **notebooks** e scripts Python.

Utiliza um dataset de vendas do [Kaggle](https://www.kaggle.com/datasets/vinothkannaece/sales-dataset) em um ambiente isolado e controlado para fins de estudo.

---

## 🧱 Camadas de Dados

- **Source**: dados brutos (.csv).
- **Bronze**: cópia fiel da fonte (`raw`), sem alterações.
- **Silver**: dados limpos e normalizados (sem duplicidades).
- **Gold**: modelagem em **Star Schema**, visando consumo analítico.

---

## 🧬 Modelagem Dimensional

A partir do arquivo `sales.csv`, o projeto gera na camada **Gold**:

- `dim_customer_type.parquet`
- `dim_date.parquet`
- `dim_payment_method.parquet`
- `dim_product.parquet`
- `dim_region.parquet`
- `dim_representative.parquet`
- `dim_sales_channel.parquet`
- `fact_sales.parquet`

---

## 🐥 Por que DuckDB?

O **DuckDB** é um banco de dados analítico **leve e embutido**, ideal para processamento local e ágil de dados:

- Armazenamento em colunas.
- Integração nativa com CSV e Parquet.
- Suporte a transações ACID.
- Altíssimo desempenho local.
- Não precisa de servidor.

Ideal para cenários menores ou médios que não justificam ferramentas pesadas como Spark — que, embora excelentes, devem ser reservadas para contextos de **Big Data** (>500GB ou TBs de dados).

---

## 🧪 Estrutura do Projeto

```bash
elt-duckdb-sales-poc/
│
├── data/                     # Dados locais (simula datalake)
│   ├── source/               # CSV original
│   ├── bronze/               # Raw data (copiado)
│   ├── silver/               # Dados limpos
│   └── gold/                 # Modelagem dimensional (star schema)
│
├── notebooks/               # Desenvolvimento em notebooks
│   ├── bronze_to_silver.ipynb
│   └── silver_to_gold.ipynb
│
├── scripts/                 # Scripts .py convertidos dos notebooks
│   ├── source_to_bronze.py
│   ├── bronze_to_silver.py
│   └── silver_to_gold.py
│
├── venv/                    # Ambiente virtual local
│
├── run_scripts.py           # Orquestração local simples dos scripts
├── convert_notebooks.py     # Conversor de notebooks para scripts
├── requirements.txt         # Dependências para desenvolvimento
├── Dockerfile               # Imagem Docker leve (~268MB)
└── .gitignore
```

---

## 🐳 Docker

A imagem Docker é extremamente leve (~268MB) e contém apenas o essencial:
```bash
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip duckdb

WORKDIR /app

CMD ["python", "run_scripts.py"]
```

---

## 📦 Instalação

Clone o repositório e instale as dependências para ambiente local de desenvolvimento:
```bash
git clone https://github.com/seu-usuario/elt-duckdb-sales-poc.git
cd elt-duckdb-sales-poc
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛠️ Pós-clonagem (opcional)

Após clonar o repositório, é possível converter os notebooks (`.ipynb`) para scripts Python (`.py`) utilizando o script auxiliar incluso no projeto. Embora os arquivos `.py` já estejam prontos no repositório, este passo demonstra como a conversão pode ser feita facilmente:

```bash
python convert_notebooks.py
```

---

## 🐳 Execução com Docker

Crie a imagem:
```bash
docker build -t elt-duckdb-sales .
```
Rode o container:
```bash
docker run --rm -v .:/app elt-duckdb-sales
```

---

## 🧠 Observações

 - O requirements.txt contém dependências voltadas ao desenvolvimento, especialmente para uso em Jupyter Notebooks.
 - O ambiente em Docker é minimalista, garantindo portabilidade e performance.
 - Foco na simulação de um Data Lake local, gerando arquivos .parquet como produto final.

---

## ✅ Considerações Finais

Esse projeto demonstra que é possível realizar pipelines ELT robustos, performáticos e bem modelados sem recorrer a ferramentas pesadas como Spark em todos os cenários.
Simplicidade, leveza e boas práticas ainda são viáveis — e, em muitos casos, mais adequadas.

---

## 📄 Licença

MIT
