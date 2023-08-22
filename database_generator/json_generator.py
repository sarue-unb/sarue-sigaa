import json
import os
from datetime import datetime
from config.json_descryption import FILE_PATH, OUTPUT_FILE_NAME, OUTPUT_FILE_NAME_FORMATTED

activity_database = {}

def add_item_to_database(activity_name:str, activity_values:str):
    activity_database[activity_name] = activity_values
     
def generate_json(start_year, end_year):
    current_time = datetime.now().strftime('%d-%m_(%H-%M)')

    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
        
    output_file_name = FILE_PATH + OUTPUT_FILE_NAME + str(start_year) + "-" + str(end_year) + "_" + str(current_time) + ".json"
    output_file_name_formatted = FILE_PATH + OUTPUT_FILE_NAME_FORMATTED + str(start_year) + "_" + str(end_year) + "_" + str(current_time) + ".json" 

    with open(output_file_name, "w+") as file_output:  
        json.dump(activity_database, file_output, indent=3)
        
    with open(output_file_name_formatted, "w+", encoding="utf-8") as file_output:  
        json.dump(activity_database, file_output, indent=3, ensure_ascii=False)

def get_quantity_of_activities():
    return len(activity_database)