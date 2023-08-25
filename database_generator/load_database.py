import os
import json
from config.json_descryption import *

databases = {output: {} for output in OUTPUT_NAMES}

def add_item_to_indicators_database(activity_name:str, activity_values, database_name:str = "full_database"):
    databases[database_name][activity_name] = activity_values
    databases[OUTPUT_NAMES["full_database"]][activity_name] = activity_values 

def load_database(file_name:str):
    if not os.path.exists(file_name):
        print(f"File {file_name} not found.")
        return None
    
    with open(file_name, "r", encoding="utf-8") as file:
        database = json.load(file)
        return database