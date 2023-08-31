from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *
from calculate_indicators.sorted_dictionarys import *

def get_qtd_actions_members_role(origin_database: dict) -> dict:
    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}
    indicators_info, indicators_info_month, indicators_info_month_type, indicators_info_year, indicators_info_year_type = {}, {}, {}, {}, {}

    roles, roles_month, roles_month_type, roles_year, roles_year_type = {}, {}, {}, {}, {}

    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        if "membros_da_equipe" in origin_database[code]:
            team_members = origin_database[code]["membros_da_equipe"]

            for member in team_members:
                name = member[0]
                role = member[1]

                if role not in roles:
                    roles[role] = set()
                roles[role].add(name)

                # Quantidade
                create_dictionary_place(roles_year, year, {})
                create_dictionary_place(roles_year_type, year, {})
                create_dictionary_place(roles_month, year, {})
                create_dictionary_place(roles_month_type, year, {})

                create_dictionary_place(roles_month[year], month, {})
                create_dictionary_place(roles_month_type[year], month, {})

                create_dictionary_place(roles_year_type[year], action_type, {})
                create_dictionary_place(roles_month_type[year][month], action_type, {})

                create_set_place(roles_year[year], role, name)
                create_set_place(roles_year_type[year][action_type], role, name)
                create_set_place(roles_month[year][month], role, name)
                create_set_place(roles_month_type[year][month][action_type], role, name)

                # Nome e papel
                create_dictionary_place(indicators_info_year, year, {})
                create_dictionary_place(indicators_info_year_type, year, {})
                create_dictionary_place(indicators_info_month, year, {})
                create_dictionary_place(indicators_info_month_type, year, {})

                create_dictionary_place(indicators_info_month[year], month, {})
                create_dictionary_place(indicators_info_month_type[year], month, {})

                create_dictionary_place(indicators_info_year_type[year], action_type, {})
                create_dictionary_place(indicators_info_month_type[year][month], action_type, {})

                create_dictionary_place(indicators_info, role, {})
                create_dictionary_place(indicators_info_year[year], role, {})
                create_dictionary_place(indicators_info_year_type[year][action_type], role, {})
                create_dictionary_place(indicators_info_month[year][month], role, {})
                create_dictionary_place(indicators_info_month_type[year][month][action_type], role, {})

                update_dictionary_place(indicators_info[role], name, 1)
                update_dictionary_place(indicators_info_year[year][role], name, 1)
                update_dictionary_place(indicators_info_year_type[year][action_type][role], name, 1)
                update_dictionary_place(indicators_info_month[year][month][role], name, 1)
                update_dictionary_place(indicators_info_month_type[year][month][action_type][role], name, 1)

    for role in roles:
        indicators[role] = len(roles[role])

    for year in roles_year:
        indicators_year[year] = {}
        for role in roles_year[year]:
            indicators_year[year][role] = len(roles_year[year][role])

    for year in roles_year_type:
        indicators_year_type[year] = {}
        for action_type in roles_year_type[year]:
            indicators_year_type[year][action_type] = {}
            for role in roles_year_type[year][action_type]:
                indicators_year_type[year][action_type][role] = len(roles_year_type[year][action_type][role])

    for year in roles_month:
        indicators_month[year] = {}
        for month in roles_month[year]:
            indicators_month[year][month] = {}
            for role in roles_month[year][month]:
                indicators_month[year][month][role] = len(roles_month[year][month][role])

    for year in roles_month_type:
        indicators_month_type[year] = {}
        for month in roles_month_type[year]:
            indicators_month_type[year][month] = {}
            for action_type in roles_month_type[year][month]:
                indicators_month_type[year][month][action_type] = {}
                for role in roles_month_type[year][month][action_type]:
                    indicators_month_type[year][month][action_type][role] = len(roles_month_type[year][month][action_type][role])

    return indicators, sorted_dict_indicators_month(indicators_month), sorted_dict_indicators_month_type(indicators_month_type), sorted_dict_indicators_year(indicators_year), sorted_dict_indicators_year_type(indicators_year_type), indicators_info, sorted_dict_members_month(indicators_info_month), sorted_dict_members_month_type(indicators_info_month_type), sorted_dict_members_year(indicators_info_year), sorted_dict_members_year_type(indicators_info_year_type)