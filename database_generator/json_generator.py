import json
import os
from datetime import datetime
from config.json_descryption import *

activity_database = {}

def add_item_to_database(activity_name:str, activity_values:str):
    activity_database[activity_name] = activity_values

def generate_json(start_year, end_year):
    # PASTA COM ARQUIVOS DE SAIDA
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
        
    # PASTA COM ARQUIVOS DE SAIDA QUE SERA USADO NO CALCULO DOS INDICADORES
    if not os.path.exists(FILE_PATH + FILE_PATH_CURRENT):
        os.makedirs(FILE_PATH + FILE_PATH_CURRENT)
    
    # PASTA COM ARQUIVOS O HISTORICO DE ARQUIVOS GERADOS PELO SCRIPT
    if not os.path.exists(FILE_PATH + FILE_PATH_HISTORY):
        os.makedirs(FILE_PATH + FILE_PATH_HISTORY)

    # PASTA COM ARQUIVOS DE SAIDA DOS INDICADORES
    if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS):
        os.makedirs(FILE_PATH + FILE_PATH_INDICATORS)
    
    current_time = datetime.now().strftime('%d-%m_%H-%M')

    current_output_file_name = FILE_PATH + FILE_PATH_CURRENT + FILE_NAME_CURRENT
    history_output_file_name = FILE_PATH + FILE_PATH_HISTORY + FILE_NAME_HISTORY + str(start_year) + "-" + str(end_year) + "_" + str(current_time) + ".json"

    with open(current_output_file_name, "w+", encoding="utf-8") as file_output:  
        json.dump(activity_database, file_output, indent=3, ensure_ascii=False)
    
    with open(history_output_file_name, "w+", encoding="utf-8") as file_output:
        json.dump(activity_database, file_output, indent=3, ensure_ascii=False)

def get_quantity_of_activities():
    return len(activity_database)