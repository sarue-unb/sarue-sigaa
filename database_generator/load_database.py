import os
import json
from config.json_descryption import *

full_database = {}
databases = {name: {inside_name: {} for inside_name in OUTPUT_NAMES[name].keys()} for name in OUTPUT_NAMES}

def add_item_to_indicators_database(activity_name:str, activity_values, database_name:str):
    databases[database_name][activity_name] = activity_values
    full_database[activity_name] = activity_values

def add_item_to_private_database(activity_name:str, activity_values, database_name:str):
    databases[database_name][activity_name] = activity_values

def load_base_database():
    if os.path.exists(FILE_NAME_BASE_DATABASE):
        with open(FILE_NAME_BASE_DATABASE, "r", encoding="utf-8") as file:
            database = json.load(file)
            return database
    else:
        return {}

def load_indicators_database():
    if os.path.exists(FILE_NAME_CURRENT_DATABASE):
        with open(FILE_NAME_CURRENT_DATABASE, "r", encoding="utf-8") as file:
            database = json.load(file)
            return database
    else:
        return {}

def generate_indicators_database():
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)
    
    if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS):
        os.mkdir(FILE_PATH + FILE_PATH_INDICATORS)

    for name in OUTPUT_NAMES:
        if not os.path.exists(FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name]):
            os.mkdir(FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name])

        for inside_name in OUTPUT_NAMES[name]:
            file_name = FILE_PATH + FILE_PATH_INDICATORS + INDICATORS_NAMES[name] + inside_name + ".json"

            with open(file_name, "w+", encoding="utf-8") as file_output:  
                json.dump(databases[name][inside_name], file_output, indent=3, ensure_ascii=False)

    with open(FILE_NAME_FULL_DATABASE, "w+", encoding="utf-8") as file_output:
        json.dump(full_database, file_output, indent=3, ensure_ascii=False)