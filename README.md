# Etanol & Fuel Stocks — Data Engineering and Analysis Pipeline

Projeto de Engenharia de Dados e Análise de Dados que investiga a relação entre o preço do etanol (CEPEA) e o valor das ações de empresas do setor de combustíveis da B3.

O projeto implementa um pipeline completo de dados, desde a coleta automatizada até a disponibilização via API REST e dashboards analíticos.

---

## 🎯 Objetivo

Identificar, através de análises estatísticas e modelagem de dados, se existe relação entre o preço do etanol e o comportamento das ações de empresas como:

* PETR4 (Petrobras)
* RAIZ4 (Raízen)
* VBBR3 (Vibra Energia)
* UGPA3 (Ultrapar)

---

## 🏗️ Arquitetura do Projeto

```
Extract (CEPEA / yfinance)
        ↓
Raw Data (CSV)
        ↓
Transform (pandas)
        ↓
PostgreSQL Data Warehouse (Star Schema)
        ↓
Análise (Python / Power BI)
        ↓
API REST (FastAPI)
```

---

## 🧱 Estrutura de Pastas

```
src/
 ├── extract
 ├── transform
 ├── load
 └── api

data/
 ├── raw
 └── processed

sql/
notebooks/
logs/
docker/
```

---

## 🛠️ Tecnologias Utilizadas

* Python (pandas, yfinance, selenium)
* PostgreSQL
* FastAPI
* Docker
* Power BI
* Git & GitHub

---

## 📊 Análises Realizadas

* Correlação de Pearson
* Regressão Linear
* Análise com defasagem temporal (LAG)
* Visualização de séries temporais
* Heatmap de correlação

---

## 🚀 Próximas Etapas

* Implementação dos scripts de extração
* Modelagem do Data Warehouse
* Criação da API REST
* Orquestração com Airflow
