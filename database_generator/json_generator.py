import json

activity_database = {}

def add_item_to_database(activity_name:str, activity_values:str):
    activity_database[activity_name] = activity_values
    
def generate_json():
    file_output = open("extension_activity_database", "w")
    json.dump(activity_database, file_output, indent=3)