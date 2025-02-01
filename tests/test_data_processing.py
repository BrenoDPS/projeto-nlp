import pytest
import pandas as pd
import sys
from pathlib import Path
from src.data_processing.mesclar_datasets import validar_df, carregar_csv

dir_raiz = Path(__file__).resolve().parents[1]
sys.path.append(str(dir_raiz))


@pytest.fixture
def valid_csv_1(tmp_path):
    """Cria um CSV válido para teste."""
    csv_path = tmp_path / "dataset1.csv"
    data = {
        "CMPLID": ["807752", "807753"],
        "ODINO": ["10350255", "10350252"],
        "LDATE": ["20140115", "20150220"],
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def valid_csv_2(tmp_path):
    """Cria outro CSV válido para teste."""
    csv_path = tmp_path / "dataset2.csv"
    data = {
        "CMPLID": ["807754", "807755"],
        "ODINO": ["10350256", "10350257"],
        "LDATE": ["20160330", "20170405"],
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def csv_errado(tmp_path):
    """Cria um CSV com schema com erros (coluna faltante)."""
    csv_path = tmp_path / "invalid.csv"
    data = {"CMPLID": ["807756"], "ODINO": ["10350258"]}  # Falta 'LDATE'
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    return csv_path


# Testes
def test_validar_df_correto():
    """Testa a validação de schema correto."""
    df = pd.DataFrame({"CMPLID": ["1"], "ODINO": ["2"], "LDATE": ["3"]})
    assert validar_df(df, ["CMPLID", "ODINO", "LDATE"]) is True


def test_validar_df_errado():
    """Testa a detecção de schema incorreto."""
    df = pd.DataFrame({"CMPLID": ["1"], "ODINO": ["2"]})  # Falta 'LDATE'
    assert validar_df(df, ["CMPLID", "ODINO", "LDATE"]) is False


def test_carregar_csv_correto(valid_csv_1):
    """Testa o carregamento de um CSV válido."""
    expected_columns = ["CMPLID", "ODINO", "LDATE"]
    df = carregar_csv(valid_csv_1, expected_columns)
    assert not df.empty
    assert list(df.columns) == expected_columns


def test_carregar_csv_errado(csv_errado):
    """Testa o tratamento de CSV com schema inválido."""
    with pytest.raises(ValueError, match="Colunas faltantes: {'LDATE'}"):
        carregar_csv(csv_errado, ["CMPLID", "ODINO", "LDATE"])
