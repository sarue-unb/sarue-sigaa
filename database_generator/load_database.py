# load_database.py
## @file
# Módulo com funções para carregar e gerar bancos de dados.
import os
import json
from datetime import datetime
from config.json_descryption import *

## Dicionário para armazenar a base de dados completa.
full_database = {}
## Dicionário de dicionários para armazenar diferentes bancos de dados.
databases = {name: {inside_name: {} for inside_name in OUTPUT_NAMES[name].keys()} for name in OUTPUT_NAMES}

## Adiciona uma atividade ao banco de dados de indicadores.
def add_item_to_indicators_database(activity_name:str, activity_values, database_name:str):
    databases[database_name][activity_name] = activity_values
    full_database[activity_name] = activity_values

## Adiciona uma atividade ao banco de dados privado.
def add_item_to_private_database(activity_name:str, activity_values, database_name:str):
    databases[database_name][activity_name] = activity_values

## Carrega a base de dados completa.
def load_base_database():
    if os.path.exists(FILE_NAME_BASE_DATABASE):
        with open(FILE_NAME_BASE_DATABASE, "r", encoding="utf-8") as file:
            database = json.load(file)
            return database
    else:
        return {}

## Carrega o banco de dados de indicadores.
def load_indicators_database():
    if os.path.exists(FILE_NAME_CURRENT_DATABASE):
        with open(FILE_NAME_CURRENT_DATABASE, "r", encoding="utf-8") as file:
            database = json.load(file)
            return database
    else:
        return {}

## Gera o banco de dados de indicadores.
def generate_indicators_database():
    ## Verifica se a pasta principal de saída existe, senão cria.
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)
    
    ## Verifica se a pasta de indicadores existe, senão cria.
    if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS):
        os.mkdir(FILE_PATH + FILE_PATH_INDICATORS)

    ## Itera sobre os nomes dos indicadores.
    for name in OUTPUT_NAMES:
        ## Verifica se a pasta de indicadores específica para o nome existe, senão cria.
        if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name]):
            os.mkdir(FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name])

        ## Itera sobre os nomes internos dos indicadores.
        for inside_name in OUTPUT_NAMES[name]:
            file_name = FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name] + inside_name + ".json"

            ## Salva o banco de dados específico para o indicador em um arquivo JSON.
            with open(file_name, "w+", encoding="utf-8") as file_output:  
                json.dump(databases[name][inside_name], file_output, indent=3, ensure_ascii=False)

    ## Adiciona a data e hora atual ao dicionário de base de dados completa.
    full_database["date_time"] =  datetime.now().strftime('%d-%m-%y_%H-%M')

    ## Salva o banco de dados completo em um arquivo JSON.
    with open(FILE_NAME_FULL_DATABASE, "w+", encoding="utf-8") as file_output:
        json.dump(full_database, file_output, indent=3, ensure_ascii=False)
