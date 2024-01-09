# database_updater.py

## @file
# Módulo para atualizar bancos de dados.

## Atualiza um banco de dados com informações mais recentes.
# @param current_database Banco de dados atual.
# @param previous_database Banco de dados anterior.
# @return Novo banco de dados atualizado.
def update_database(current_database:dict, previous_database:dict) -> dict:
    new_database = {}

    new_database.update(previous_database)
    new_database.update(current_database)

    new_database = sorted_database(new_database)
    return new_database

## Ordena um banco de dados com base nas chaves.
# @param database Banco de dados a ser ordenado.
# @return Banco de dados ordenado.
def sorted_database(database:dict) -> dict:
    sorted_database = {}

    sorted_keys = sorted(database.keys(), key=lambda x: (int(x.split('-')[1][:4:]), x.split('-')[0]))
    
    for key in sorted_keys:
        sorted_database[key] = database[key]

    return sorted_database
