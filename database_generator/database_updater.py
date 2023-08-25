def update_database(current_database:dict, previous_database:dict) -> dict:
    new_database = {}

    new_database.update(previous_database)
    new_database.update(current_database)

    return new_database