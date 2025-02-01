"""
Script para unir múltiplos datasets do NHTSA em um único arquivo CSV.
Garante validação de dados e logs detalhados.
"""

import pandas as pd
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("data/logs/merge_logs.log"), logging.StreamHandler()]
)

def validar_df(df: pd.DataFrame, col_esp: list):
    """Valida se o DataFrame possui as colunas esperadas."""
    return all(col in df.columns for col in col_esp)


def carregar_csv(path: Path, col_esp: list):
    """Carrega e valida um arquivo CSV."""
    try:
        df = pd.read_csv(
            path,
            dtype=str,
            encoding='utf-8'
        )
        
        # Validação do DataFrame
        if not validar_df(df, col_esp):
            falt = set(col_esp) - set(df.columns)
            raise ValueError(f"Colunas faltantes: {falt}")
        
        if 'LDATE' in df.columns:
            df['LDATE'] = pd.to_datetime(df['LDATE'], format='%Y%m%d', errors='coerce')
            
        logging.info(f"CSV carregado: {path.name} | Registros: {len(df):,}")
        return df

    except Exception as e:
        logging.error(f"Falha ao carregar {path.name}: {str(e)}")
        raise


def mesclar_datasets(entrada: Path, saida: Path):
    """Une todos os CSV em um diretório."""
    # Listar arquivos CSV
    arq_csv = list(entrada.glob("*.csv"))
    if not arq_csv:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado para unir.")
    
    # Carregar primeiro arquivo para obter schema
    df_aux = carregar_csv(arq_csv[0], col_esp=[])
    col_esp = df_aux.columns.tolist()
    
    # Carregar e validar todos os arquivos
    df_mesclado = pd.DataFrame(columns=col_esp)
    
    for arq in arq_csv:
        df = carregar_csv(arq, col_esp)
        df_mesclado = pd.concat([df_mesclado, df], axis=0, ignore_index=True)
    
    # Validações finais
    if df_mesclado.empty:
        raise ValueError("Dataset combinado está vazio.")
        
    logging.info(f"""
    Dataset final consolidado:
    - Total de registros: {len(df_mesclado):,}
    - Período temporal: {df_mesclado['LDATE'].min()} a {df_mesclado['LDATE'].max()}
    - Colunas: {list(df_mesclado.columns)}
    """)
    
    # Salvar resultado
    saida.parent.mkdir(parents=True, exist_ok=True)
    df_mesclado.to_csv(saida, index=False)
    logging.info(f"Dataset consolidado salvo em: {saida}")

if __name__ == "__main__":
    # Configuração de paths
    dir_raiz = Path(__file__).resolve().parents[2]
    entrada = dir_raiz / "data" / "interim"  # Pasta com CSVs individuais
    saida = dir_raiz / "data" / "processed" / "reclamacoes.csv"
    
    try:
        mesclar_datasets(entrada, saida)
    except Exception as e:
        logging.critical(f"Falha na união: {str(e)}")
        raise


# def null_values(data: pd.DataFrame):

#     # função que calcula a pct de valores nulos em cada coluna

#     pct = (data.isnull().sum() / data.shape[0] ) * 100

#     return pct.round(2)