import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
OUTPUT_PATH = RAW_PATH / "etanol_padronizado.csv"


def extract_etanol_excel():
    file_path = RAW_PATH / "cepea-consulta-dadosbrutos.xlsx"

    # Lê o Excel pulando as 3 primeiras linhas
    df = pd.read_excel(file_path, skiprows=3)

    # Renomeia colunas
    df.columns = ["data", "preco_real", "preco_dolar"]

    # Converte data
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    # Remove linhas inválidas
    df = df.dropna()

    # Ordena por data
    df = df.sort_values("data")

    # Salva CSV padronizado
    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Etanol extraído e padronizado com sucesso!")
    print(df.head())


if __name__ == "__main__":
    extract_etanol_excel()

