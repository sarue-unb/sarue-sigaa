import json
import os
import time
from datetime import datetime
from config.json_descryption import *
from config.crawler_descryption import TYPE_BASE, SCHEDULE
from config.display_descryption import centralize, clear_screen, SLEEP_TIME
from database_generator.load_database import load_base_database
from database_generator.database_updater import update_database

current_activity_database = {}
previous_activity_database = {}
full_activity_database = {}

def add_item_to_crawler_database(activity_name:str, activity_values:str):
    current_activity_database[activity_name] = activity_values

def generate_crawler_json(start_year, end_year):
    # PASTA COM ARQUIVOS DE SAIDA
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)

    # PASTA COM A BASE DE DADOS
    if not os.path.exists(FILE_PATH + FILE_PATH_BASE):
        os.makedirs(FILE_PATH + FILE_PATH_BASE)
        
    # PASTA COM O ATUAL ARQUIVO DE CALCULAR INDICADORES
    if not os.path.exists(FILE_PATH + FILE_PATH_CURRENT):
        os.makedirs(FILE_PATH + FILE_PATH_CURRENT)
    
    # PASTA COM ARQUIVOS O HISTORICO DE ARQUIVOS GERADOS PELO SCRIPT
    if not os.path.exists(FILE_PATH + FILE_PATH_HISTORY):
        os.makedirs(FILE_PATH + FILE_PATH_HISTORY)

    # PASTA COM ARQUIVOS DE SAIDA DOS INDICADORES
    if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS):
        os.makedirs(FILE_PATH + FILE_PATH_INDICATORS)
    
    current_time = datetime.now().strftime('%d-%m_%H-%M')

    history_output_file_name = FILE_NAME_HISTORY_DATABASE + str(start_year) + "-" + str(end_year) + "_" + str(current_time) + ".json"

    if TYPE_BASE == 'FULL':
        # Obter tudo e gerar um base também
        pass
    elif TYPE_BASE == 'REBASE':
        previous_activity_database = load_base_database()
        full_base_database = update_database(current_activity_database, previous_activity_database)
        
        len_previous_activity_database = len(previous_activity_database)
        len_current_activity_database = len(current_activity_database)
        len_full_base_database = len(full_base_database)

        if SCHEDULE == True:
            clear_screen()
            centralize(("Quantidade de atividades na base anterior: " + str(len_previous_activity_database)))
            centralize(("Quantidade de atividades na base atual: " + str(len_current_activity_database)))
            centralize(("Quantidade de atividades na base conjunta: " + str(len_full_base_database)))
            
            time.sleep(SLEEP_TIME)
            with open(FILE_NAME_BASE_DATABASE, "w+", encoding="utf-8") as file_output:
                json.dump(full_base_database, file_output, indent=3, ensure_ascii=False) 
                
        else:
            clear_screen()
            centralize(("Quantidade de atividades na base anterior: " + str(len_previous_activity_database)))
            centralize(("Quantidade de atividades na base atual: " + str(len_current_activity_database)))
            centralize(("Quantidade de atividades na base conjunta: " + str(len_full_base_database)))
            
            entrada = input("Deseja atualizar a base? (S/N): ")
            if entrada == 'S' or entrada == 's':
                with open(FILE_NAME_BASE_DATABASE, "w+", encoding="utf-8") as file_output:
                    json.dump(full_base_database, file_output, indent=3, ensure_ascii=False) 
                
    elif TYPE_BASE == 'BASE':
        previous_activity_database = load_base_database()
        full_activity_database = update_database(current_activity_database, previous_activity_database)

        # Gear arquivo completo com a base e o atual
        with open(FILE_NAME_CURRENT_DATABASE, "w+", encoding="utf-8") as file_output:  
            json.dump(full_activity_database, file_output, indent=3, ensure_ascii=False)
        
        # Gerar arquivo de historico
        with open(history_output_file_name, "w+", encoding="utf-8") as file_output:
            json.dump(current_activity_database, file_output, indent=3, ensure_ascii=False)

def get_quantity_of_activities():
    return len(current_activity_database)

def clear_screen():
    if os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
        _ = os.system('clear')
    else:  # Para o Windows
        _ = os.system('cls')