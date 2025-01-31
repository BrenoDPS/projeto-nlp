"""
Script para conversão segura de arquivos .txt (tabulação) para .csv.
Garante a preservação da estrutura de dados e validação de integridade.
"""

import pandas as pd
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Lista de colunas baseada na documentação fornecida
COLUMN_NAMES = [
    'CMPLID', 'ODINO', 'MFR_NAME', 'MAKETXT', 'MODELTXT', 'YEARTXT', 'CRASH',
    'FAILDATE', 'FIRE', 'INJURED', 'DEATHS', 'COMPDESC', 'CITY', 'STATE', 'VIN',
    'DATEA', 'LDATE', 'MILES', 'OCCURENCES', 'CDESCR', 'CMPL_TYPE', 'POLICE_RPT_YN',
    'PURCH_DT', 'ORIG_OWNER_YN', 'ANTI_BRAKES_YN', 'CRUISE_CONT_YN', 'NUM_CYLS',
    'DRIVE_TRAIN', 'FUEL_SYS', 'FUEL_TYPE', 'TRANS_TYPE', 'VEH_SPEED', 'DOT',
    'TIRE_SIZE', 'LOC_OF_TIRE', 'TIRE_FAIL_TYPE', 'ORIG_EQUIP_YN', 'MANUF_DT',
    'SEAT_TYPE', 'RESTRAINT_TYPE', 'DEALER_NAME', 'DEALER_TEL', 'DEALER_CITY',
    'DEALER_STATE', 'DEALER_ZIP', 'PROD_TYPE', 'REPAIRED_YN', 'MEDICAL_ATTN',
    'VEHICLES_TOWED_YN'
]

def validate_input_file(input_path: Path) -> None:
    """Valida a existência e extensão do arquivo de entrada."""
    if not input_path.exists():
        raise FileNotFoundError(f'Arquivo não encontrado: {input_path}')
    if input_path.suffix != '.txt':
        raise ValueError(f'Extensão inválida: {input_path.suffix} (esperado .txt)')

def convert_txt_to_csv(input_path: Path, output_dir: Path) -> None:
    """
    Converte um arquivo .txt para .csv com tratamento de erros.
    
    Args:
        input_path: Caminho para o arquivo .txt de entrada
        output_dir: Diretório para salvar o arquivo .csv resultante
    """
    try:
        # Carregar dados com tratamento de erros
        df = pd.read_csv(
            input_path,
            sep='\t',
            header=None,
            names=COLUMN_NAMES,
            dtype=str,
            on_bad_lines='warn',
            encoding='utf-8'
        )
        
        # Criar diretório de saída se necessário
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Gerar caminho de saída
        output_path = output_dir / f'{input_path.stem}.csv'
        
        # Salvar como CSV
        df.to_csv(output_path, index=False, encoding='utf-8')
        logging.info(f'Conversão concluída: {input_path} -> {output_path}')
        
    except Exception as e:
        logging.error(f'Erro ao processar {input_path}: {str(e)}')
        raise

def main():
    # Configurar paths
    project_root = Path(__file__).resolve().parents[2]  # Ajustar conforme estrutura
    raw_data_dir = project_root / 'data' / 'raw'
    interim_data_dir = project_root / 'data' / 'interim'

    # Processar todos os arquivos .txt no diretório raw
    for txt_file in raw_data_dir.glob('*.txt'):
        try:
            validate_input_file(txt_file)
            convert_txt_to_csv(txt_file, interim_data_dir)
        except Exception as e:
            logging.error(f'Falha ao processar {txt_file.name}: {str(e)}')
            continue

if __name__ == '__main__':
    main()