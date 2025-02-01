import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture(scope="module")
def sample_data():
    """Carrega um dataset pequeno para testes rápidos."""
    data_path = Path(__file__).parent / "fixtures/sample_data.csv"
    return pd.read_csv(data_path)

@pytest.fixture
def raw_dataframe():
    """Simula um DataFrame bruto para testes de pré-processamento."""
    return pd.DataFrame({
        'CDESCR': ['Brake failure *TR', 'Engine overheating...'],
        'LDATE': ['20140115', '20150220'],
        'CRASH': ['N', 'Y']
    })