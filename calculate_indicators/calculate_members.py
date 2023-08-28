from config.date_descryption import DIGITS_MONTHS

def sorted_dict_indicators_month(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in dictionary:
        for month in sorted(dictionary[year], key=lambda x: list(DIGITS_MONTHS.values()).index(x) if x != "anual" else 0):
            for item in sorted(dictionary[year][month]):
                if year not in r_dictionary:
                    r_dictionary[year] = {}
                if month not in r_dictionary[year]:
                    r_dictionary[year][month] = {}
                r_dictionary[year][month][item] = dictionary[year][month][item]

    return r_dictionary

def sorted_dict_indicators_year(dictionary: dict) -> dict:
    r_dictionary = {}
    for year in sorted(dictionary):
        for item in sorted(dictionary[year]):
                if year not in r_dictionary:
                    r_dictionary[year] = {}
                r_dictionary[year][item] = dictionary[year][item]

    return r_dictionary