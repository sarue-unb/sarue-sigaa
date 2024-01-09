# excel_generator.py
## @file
# Essa função gera um arquivo Excel a partir de um banco de dados em formato JSON.

import pandas as pd
import openpyxl
from config.json_descryption import FILE_NAME_CURRENT_DATABASE, FILE_NAME_EXCEL_DATABASE

## Gera um arquivo Excel a partir de um banco de dados em formato JSON.
def generate_excel_database():
    ## Nome do arquivo JSON contendo o banco de dados atual.
    json_file = FILE_NAME_CURRENT_DATABASE
    ## Lê os dados do arquivo JSON.
    data = pd.read_json(json_file)

    ## Transpõe os dados para que as chaves do dicionário se tornem colunas.
    data_transposed = data.T
  
    ## Nome do arquivo Excel a ser gerado.
    xlsx_file = FILE_NAME_EXCEL_DATABASE
    ## Salva os dados transpostos no arquivo Excel.
    data_transposed.to_excel(xlsx_file, index=True)
