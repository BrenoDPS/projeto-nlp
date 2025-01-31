"""
Filtra o dataset para manter apenas reclamações a partir de 01/01/2014.
Remove registros com datas inválidas ou fora do intervalo.
"""

import pandas as pd
from pathlib import Path
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data de corte (inclusive)
DATA_DE_CORTE = pd.to_datetime("2014-01-01")

def carrega_dados(entrada: Path) -> pd.DataFrame:
    """Carrega o CSV e converte 'LDATE' para datetime."""
    df = pd.read_csv(entrada, parse_dates=['LDATE'], dayfirst=False, infer_datetime_format=True)
    
    # Verificar conversão
    if not pd.api.types.is_datetime64_any_dtype(df['LDATE']):
        raise ValueError("Falha na conversão de 'LDATE' para datetime.")
    
    return df

def filtra_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra dados anteriores a 2014-01-01 e remove datas inválidas."""
    # Filtrar datas válidas e >= DATA_DE_CORTE
    df_filt = df[df['LDATE'] >= DATA_DE_CORTE]
    
    # Remover registros com datas inválidas (NaT)
    tam_original = len(df)
    tam_filt = len(df_filt)
    tam_final = tam_original - tam_filt
    
    logging.info(
        f"Registros removidos: {tam_final} "
        f"({tam_final/tam_original:.1%} do total)"
    )
    
    return df_filt

def main():
    # Configurar paths
    entrada = Path('../../data/interim/COMPLAINTS_RECEIVED_2010-2014.csv')
    saida = Path('../../data/interim/COMPLAINTS_RECEIVED_2014.csv')
    
    try:
        # Carregar e filtrar
        df = carrega_dados(entrada)
        df_filt = filtra_dados(df)
        
        # Salvar
        saida.parent.mkdir(parents=True, exist_ok=True)
        df_filt.to_csv(saida, index=False)
        logging.info(f"Dataset filtrado salvo em: {saida}")
        
    except Exception as e:
        logging.error(f"Erro crítico: {str(e)}")
        raise

if __name__ == '__main__':
    main()