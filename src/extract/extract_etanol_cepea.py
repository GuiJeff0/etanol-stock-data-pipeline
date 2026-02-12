from seleniumbase import SB
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

from src.config.settings import (URL, TABLE_ID)

RAW_PATH = Path("data/raw")
OUTPUT_FILE = RAW_PATH / "cepea_etanol_latest.csv"


def bypass_verification(sb):
    try:
        sb.assert_element(f"#{TABLE_ID}", timeout=8)
    except Exception:
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.uc_click('input[value*="Verify"]')
        else:
            sb.uc_gui_click_captcha()


def extrair_dados():
    with SB(uc=True, headed=True) as sb:

        sb.uc_open_with_reconnect(URL, reconnect_time=4)
        bypass_verification(sb)

        sb.sleep(3)

        tabela = sb.find_element(f"#{TABLE_ID}")

        headers = tabela.find_elements("tag name", "th")
        columns = [h.text.strip() for h in headers]
        columns[0] = "Periodo"

        rows = tabela.find_elements("tag name", "tr")
        data = []

        for row in rows[1:]:
            tds = row.find_elements("tag name", "td")
            if len(tds) == len(columns) and "imagenet-tbl-esconder" not in row.get_attribute("class"):
                values = [td.text.strip() for td in tds]
                data.append(values)

        if not data:
            raise RuntimeError("Nenhuma linha válida")

        return pd.DataFrame(data, columns=columns)

def padronizar_periodo(df: pd.DataFrame):

    # Extrai apenas a parte da data (depois do hífen)
    df["Periodo"] = df["Periodo"].str.split("-").str[-1].str.strip()

    # Converte para datetime
    df["Periodo"] = pd.to_datetime(df["Periodo"], dayfirst=True)

    # Formata como YYYY-MM-DD
    df["Periodo"] = df["Periodo"].dt.strftime("%Y-%m-%d")

    return df


def salvar_arquivo(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)
    print(f"Salvo: {file_path}")


if __name__ == "__main__":
    dataframe = extrair_dados()
    dataframe = padronizar_periodo(dataframe)
    salvar_arquivo(dataframe, OUTPUT_FILE)