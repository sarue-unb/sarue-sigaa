def update_database(current_database:dict, previous_database:dict) -> dict:
    new_database = {}

    new_database.update(previous_database)
    new_database.update(current_database)

    new_database = sorted_database(new_database)
    return new_database

def sorted_database(database:dict) -> dict:
    sorted_database = {}

    sorted_keys = sorted(database.keys(), key=lambda x: (int(x.split('-')[1][:4:]), x.split('-')[0]))
    
    for key in sorted_keys:
        sorted_database[key] = database[key]

    return sorted_database