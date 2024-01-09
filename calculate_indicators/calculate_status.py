# calculate_status.py
## @file
# Módulo para calcular todos os indicadores relacionados aos status das ações.

from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *
from calculate_indicators.sorted_dictionarys import *

def get_qtd_actions_status(origin_database: dict) -> tuple[dict, dict, dict, dict, dict]:
    """
        Calcula a quantidade de ações para cada status em diferentes períodos e tipos.

        Esta função recebe um banco de dados de origem como entrada e calcula a quantidade de ações para cada status nos
        seguintes períodos e tipos: geral, anual, mensal, anual com tipo de ação e mensal com tipo de ação.

        @param origin_database: Banco de dados de entrada contendo informações sobre as ações.
        @return: Uma tupla contendo dicionários para os indicadores de geral, anual, mensal, anual com tipo de ação e mensal com
                tipo de ação.
    """

    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}
    
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]
        status = origin_database[code]["situacao"]

        create_dictionary_place(indicators_year, year, {})
        create_dictionary_place(indicators_year_type, year, {})
        create_dictionary_place(indicators_month, year, {})
        create_dictionary_place(indicators_month_type, year, {})

        create_dictionary_place(indicators_month[year], month, {})
        create_dictionary_place(indicators_month_type[year], month, {})

        create_dictionary_place(indicators_year_type[year], action_type, {})
        create_dictionary_place(indicators_month_type[year][month], action_type, {})

        update_dictionary_place(indicators, status, 1)
        update_dictionary_place(indicators_year[year], status, 1)
        update_dictionary_place(indicators_year_type[year][action_type], status, 1)
        update_dictionary_place(indicators_month[year][month], status, 1)
        update_dictionary_place(indicators_month_type[year][month][action_type], status, 1)

        indicators_month = sorted_dict_year_month(indicators_month)
        indicators_month_type = sorted_dict_indicators_month(indicators_month_type)

    return indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type
