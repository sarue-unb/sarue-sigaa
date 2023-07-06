import json
import os

from datetime import datetime
from components.database_formatter import format_special_char

activity_database = {}

def add_item_to_database(activity_name:str, activity_values:str):
    activity_database[activity_name] = activity_values
    
def generate_json(start_year, end_year):
    current_time = datetime.now().strftime('%H:%M:%S')
    
    file_path = "database/"

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = file_path + "extension_activity_database_" + str(start_year) + "_" + str(end_year) + "_" + str(current_time)
    file_name = file_name.replace(":", "-") + ".json"
    
    with open(file_name, "w+") as file_output:  
        json.dump(activity_database, file_output, indent=3)
        
    format_special_char(file_name)

    