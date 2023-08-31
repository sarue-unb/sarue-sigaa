from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *
from calculate_indicators.sorted_dictionarys import *

def get_qtd_actions_status(origin_database: dict) -> dict:
    indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]
        status = origin_database[code]["situacao"]

        create_dictionary_place(indicators_year, year, {})
        update_dictionary_place(indicators_year[year], status, 1)

        create_dictionary_place(indicators_year_type, year, {})
        create_dictionary_place(indicators_year_type[year], action_type, {})
        update_dictionary_place(indicators_year_type[year][action_type], status, 1)

        create_dictionary_place(indicators_month, year, {})
        create_dictionary_place(indicators_month[year], month, {})
        update_dictionary_place(indicators_month[year][month], status, 1)

        create_dictionary_place(indicators_month_type, year, {})
        create_dictionary_place(indicators_month_type[year], month, {})
        create_dictionary_place(indicators_month_type[year][month], action_type, {})
        update_dictionary_place(indicators_month_type[year][month][action_type], status, 1)

    return sorted_dict_year_month(indicators_month), sorted_dict_indicators_month(indicators_month_type), indicators_year, indicators_year_type