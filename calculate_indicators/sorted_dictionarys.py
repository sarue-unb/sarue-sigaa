from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *

def sorted_dict(dictionary: dict) -> dict:
    r_dictionary = {}
    for item in sorted(dictionary):
        r_dictionary[item] = dictionary[item]
    return r_dictionary

def sorted_dict_year_month(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x)):
            if year not in r_dictionary:
                r_dictionary[year] = {}
            r_dictionary[year][month] = dictionary[year][month]
    return r_dictionary

def sorted_dict_indicators_month(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for item in sorted(dictionary[year][month]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], month, {})
                r_dictionary[year][month][item] = dictionary[year][month][item]

    return r_dictionary

def sorted_dict_indicators_month_type(dictionary: dict) -> dict:
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

def sorted_dict_indicators_year(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in sorted(dictionary):
        for item in sorted(dictionary[year]):
            create_dictionary_place(r_dictionary, year, {})
            r_dictionary[year][item] = dictionary[year][item]

    return r_dictionary

def sorted_dict_indicators_year_type(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in sorted(dictionary):
        for action_type in sorted(dictionary[year]):
            for item in sorted(dictionary[year][action_type]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], action_type, {})
                r_dictionary[year][action_type][item] = dictionary[year][action_type][item]

    return r_dictionary

def sorted_dict_members_month(dictionary: dict) -> dict:
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

def sorted_dict_members_month_type(dictionary: dict) -> dict:
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

def sorted_dict_members_year(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in sorted(dictionary):
        for item in sorted(dictionary[year]):
            for name in sorted(dictionary[year][item]):
                create_dictionary_place(r_dictionary, year, {})
                create_dictionary_place(r_dictionary[year], item, {})
                r_dictionary[year][item][name] = dictionary[year][item][name]

    return r_dictionary

def sorted_dict_members_year_type(dictionary: dict) -> dict:
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