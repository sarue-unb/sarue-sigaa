import pandas as pd
import openpyxl
from config.json_descryption import FILE_NAME_CURRENT_DATABASE, FILE_NAME_EXCEL_DATABASE

def generate_excel_database():
    json_file = FILE_NAME_CURRENT_DATABASE
    data = pd.read_json(json_file)

    data_transposed = data.T
  
    xlsx_file = FILE_NAME_EXCEL_DATABASE
    data_transposed.to_excel(xlsx_file, index=True)