# sorted_dictionarys.py
## @file
# Módulo com funções para ordenar dicionários.

from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *

# Função para ordenar um dicionário com base nas chaves.
def sorted_dict(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base nas chaves.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base nas chaves.
    """
    r_dictionary = {}
    for item in sorted(dictionary):
        r_dictionary[item] = dictionary[item]
    return r_dictionary

# Função para ordenar um dicionário com base no ano e mês.
def sorted_dict_year_month(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base no ano e mês.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base no ano e mês.
    """
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x)):
            create_dictionary_place(r_dictionary, year, {})
            r_dictionary[year][month] = dictionary[year][month]

    return r_dictionary

# Função para ordenar um dicionário com base em indicadores e mês.
def sorted_dict_indicators_month(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em indicadores e mês.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em indicadores e mês.
    """
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for item in sorted(dictionary[year][month]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], month, {})
                r_dictionary[year][month][item] = dictionary[year][month][item]

    return r_dictionary

# Função para ordenar um dicionário com base em indicadores, mês e tipo de ação.
def sorted_dict_indicators_month_type(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em indicadores, mês e tipo de ação.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em indicadores, mês e tipo de ação.
    """
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for action_type in sorted(dictionary[year][month]):
                for item in sorted(dictionary[year][month][action_type]):
                    create_dictionary_place(r_dictionary, year, {})
                    create_dictionary_place(r_dictionary[year], month, {})
                    create_dictionary_place(r_dictionary[year][month], action_type, {})
                    r_dictionary[year][month][action_type][item] = dictionary[year][month][action_type][item]

    return r_dictionary

# Função para ordenar um dicionário com base em indicadores e ano.
def sorted_dict_indicators_year(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em indicadores e ano.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em indicadores e ano.
    """
    r_dictionary = {}
    for year in sorted(dictionary):
        for item in sorted(dictionary[year]):
            create_dictionary_place(r_dictionary, year, {})
            r_dictionary[year][item] = dictionary[year][item]

    return r_dictionary

# Função para ordenar um dicionário com base em indicadores, ano e tipo de ação.
def sorted_dict_indicators_year_type(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em indicadores, ano e tipo de ação.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em indicadores, ano e tipo de ação.
    """
    r_dictionary = {}
    for year in sorted(dictionary):
        for action_type in sorted(dictionary[year]):
            for item in sorted(dictionary[year][action_type]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], action_type, {})
                r_dictionary[year][action_type][item] = dictionary[year][action_type][item]

    return r_dictionary

# Função para ordenar um dicionário com base em membros e tipo de ação.
def sorted_dict_members_type(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em membros e tipo de ação.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em membros e tipo de ação.
    """
    r_dictionary = {}
    for action_type in sorted(dictionary):
        for name in sorted(dictionary[action_type]):
            create_dictionary_place(r_dictionary, action_type, {})
            r_dictionary[action_type][name] = dictionary[action_type][name]

    return r_dictionary

# Função para ordenar um dicionário com base em membros, mês e tipo de ação.
def sorted_dict_members_month(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em membros, mês e tipo de ação.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em membros, mês e tipo de ação.
    """
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for item in sorted(dictionary[year][month]):
                for name in sorted(dictionary[year][month][item]):
                    create_dictionary_place(r_dictionary, year, {})
                    create_dictionary_place(r_dictionary[year], month, {})
                    create_dictionary_place(r_dictionary[year][month], item, {})
                    r_dictionary[year][month][item][name] = dictionary[year][month][item][name]

    return r_dictionary

# Função para ordenar um dicionário com base em membros, mês, tipo de ação e item.
def sorted_dict_members_month_type(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em membros, mês, tipo de ação e item.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em membros, mês, tipo de ação e item.
    """
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for action_type in sorted(dictionary[year][month]):
                for item in sorted(dictionary[year][month][action_type]):
                    for name in sorted(dictionary[year][month][action_type][item]):
                        create_dictionary_place(r_dictionary, year, {})
                        create_dictionary_place(r_dictionary[year], month, {})
                        create_dictionary_place(r_dictionary[year][month], action_type, {})
                        create_dictionary_place(r_dictionary[year][month][action_type], item, {})
                        r_dictionary[year][month][action_type][item][name] = dictionary[year][month][action_type][item][name]

    return r_dictionary

# Função para ordenar um dicionário com base em membros e ano.
def sorted_dict_members_year(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em membros e ano.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em membros e ano.
    """
    r_dictionary = {}
    for year in sorted(dictionary):
        for item in sorted(dictionary[year]):
            for name in sorted(dictionary[year][item]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], item, {})
                r_dictionary[year][item][name] = dictionary[year][item][name]

    return r_dictionary

# Função para ordenar um dicionário com base em membros, ano e tipo de ação.
def sorted_dict_members_year_type(dictionary: dict) -> dict:
    """
    Ordena um dicionário com base em membros, ano e tipo de ação.

    @param dictionary: Dicionário de entrada.
    @return: Dicionário ordenado com base em membros, ano e tipo de ação.
    """
    r_dictionary = {}
    for year in sorted(dictionary):
        for action_type in sorted(dictionary[year]):
            for item in sorted(dictionary[year][action_type]):
                for name in sorted(dictionary[year][action_type][item]):
                    create_dictionary_place(r_dictionary, year, {})
                    create_dictionary_place(r_dictionary[year], action_type, {})
                    create_dictionary_place(r_dictionary[year][action_type], item, {})
                    r_dictionary[year][action_type][item][name] = dictionary[year][action_type][item][name]

    return r_dictionary