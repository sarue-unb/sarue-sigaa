import re
from config.date_descryption import DIGITS_MONTHS

def sorted_dict(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x)):
            if year not in r_dictionary:
                r_dictionary[year] = {}
            r_dictionary[year][month] = dictionary[year][month]
    return r_dictionary

def sorted_dict_info(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in dictionary:
        for action_type in dictionary[year]:
            for month in sorted(dictionary[year][action_type], key=lambda x: list(DIGITS_MONTHS.values()).index(x)):
                if year not in r_dictionary:
                    r_dictionary[year] = {}
                if action_type not in r_dictionary[year]:
                    r_dictionary[year][action_type] = {}
                r_dictionary[year][action_type][month] = dictionary[year][action_type][month]
    return r_dictionary

def get_qtd_actions_status(indicators_month: dict, indicators_month_type: dict, indicators_year: dict, indicators_year_type: dict, origin_database: dict) -> dict:
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]
        status = origin_database[code]["situacao"]

        if year not in indicators_year: #Year  
            indicators_year[year] = {}

        if status not in indicators_year[year]:
            indicators_year[year][status] = 1
        else:
            indicators_year[year][status] += 1

        if year not in indicators_year_type: #Year
            indicators_year_type[year] = {}
        if action_type not in indicators_year_type[year]:
            indicators_year_type[year][action_type] = {}
     
        if status not in indicators_year_type[year][action_type]:
            indicators_year_type[year][action_type][status] = 1
        else:
            indicators_year_type[year][action_type][status] += 1

        if year not in indicators_month: #Year
            indicators_month[year] = {}
        if month not in indicators_month[year]: 
            indicators_month[year][month] = {}

        if status not in indicators_month[year][month]: 
            indicators_month[year][month][status] = 1
        else:
            indicators_month[year][month][status] += 1

        if year not in indicators_month_type: #Year
            indicators_month_type[year] = {}
        if action_type not in indicators_month_type[year]:
            indicators_month_type[year][action_type] = {}
        if month not in indicators_month_type[year][action_type]:
            indicators_month_type[year][action_type][month] = {}

        if status not in indicators_month_type[year][action_type][month]:
            indicators_month_type[year][action_type][month][status] = 1
        else:
            indicators_month_type[year][action_type][month][status] += 1

    return sorted_dict(indicators_month), sorted_dict_info(indicators_month_type), indicators_year, indicators_year_type

def return_number(text: str) -> int:
    padrao = r'(\d+)'
    resultado = re.search(padrao, text)  # Procurar o padrão no texto

    if resultado:
        return int(resultado.group(1))  # Converter o valor encontrado para um inteiro
    else:
        return 0
    