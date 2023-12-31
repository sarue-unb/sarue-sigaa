from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.sorted_dictionarys import *

def get_qtd_actions_objectives(origin_database: dict) -> dict:
    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        if "objetivos" in origin_database[code]:
            objectives = origin_database[code]["objetivos"]


            create_dictionary_place(indicators_year, year, {})
            create_dictionary_place(indicators_year_type, year, {})

            create_dictionary_place(indicators_month, year, {})
            create_dictionary_place(indicators_month_type, year, {})

            create_dictionary_place(indicators_month[year], month, {})
            create_dictionary_place(indicators_month_type[year], month, {})

            create_dictionary_place(indicators_year_type[year], action_type, {})
            create_dictionary_place(indicators_month_type[year][month], action_type, {})

            for objective in objectives:
                update_dictionary_place(indicators, objective, 1)
                update_dictionary_place(indicators_year[year], objective, 1)
                update_dictionary_place(indicators_month[year][month], objective, 1)
                update_dictionary_place(indicators_year_type[year][action_type], objective, 1)
                update_dictionary_place(indicators_month_type[year][month][action_type], objective, 1)

    indicators = sorted_dict(indicators)
    indicators_month = sorted_dict_indicators_month(indicators_month)
    indicators_month_type = sorted_dict_indicators_month(indicators_month_type)
    indicators_year = sorted_dict_indicators_year(indicators_year)
    indicators_year_type = sorted_dict_indicators_year(indicators_year_type)

    return indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type

def get_qtd_actions_objectives_len(origin_database: dict) -> dict:
    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        if "objetivos" in origin_database[code]:
            objectives = origin_database[code]["objetivos"]

            create_dictionary_place(indicators_year, year, {})
            create_dictionary_place(indicators_year_type, year, {})

            create_dictionary_place(indicators_month, year, {})
            create_dictionary_place(indicators_month_type, year, {})

            create_dictionary_place(indicators_month[year], month, {})
            create_dictionary_place(indicators_month_type[year], month, {})

            create_dictionary_place(indicators_year_type[year], action_type, {})
            create_dictionary_place(indicators_month_type[year][month], action_type, {})

            update_dictionary_place(indicators, len(objectives), 1)
            update_dictionary_place(indicators_year[year], len(objectives), 1)
            update_dictionary_place(indicators_year_type[year][action_type], len(objectives), 1)
            update_dictionary_place(indicators_month[year][month], len(objectives), 1)
            update_dictionary_place(indicators_month_type[year][month][action_type], len(objectives), 1)

    indicators = sorted_dict(indicators)
    indicators_month = sorted_dict_indicators_month(indicators_month)
    indicators_month_type = sorted_dict_indicators_month(indicators_month_type)
    indicators_year = sorted_dict_indicators_year(indicators_year)
    indicators_year_type = sorted_dict_indicators_year(indicators_year_type)
                
    return indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type