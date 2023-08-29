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

def get_qtd_actions_objectives(origin_database: dict) -> dict:
    indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        if "objetivos" in origin_database[code]:
            objectives = origin_database[code]["objetivos"]

            if year not in indicators_year: #Year
                indicators_year[year] = {}
                indicators_year_type[year] = {}

            if year not in indicators_month: #Year
                indicators_month[year] = {}
                indicators_month_type[year] = {}

            if month not in indicators_month[year]: #Month
                indicators_month[year][month] = {}
                indicators_month_type[year][month] = {}

            if action_type not in indicators_month[year]: #Action Type
                indicators_year_type[year][action_type] = {}
            
            if action_type not in indicators_month[year][month]: #Action Type
                indicators_month_type[year][month][action_type] = {}


            for objective in objectives:
                if objective not in indicators_year[year]:
                    indicators_year[year][objective] = 1
                else:
                    indicators_year[year][objective] += 1

                if objective not in indicators_month[year][month]:
                    indicators_month[year][month][objective] = 1
                else:
                    indicators_month[year][month][objective] += 1

                if objective not in indicators_year_type[year][action_type]:
                    indicators_year_type[year][action_type][objective] = 1
                else:
                    indicators_year_type[year][action_type][objective] += 1

                if objective not in indicators_month_type[year][month][action_type]: 
                    indicators_month_type[year][month][action_type][objective] = 1
                else:
                    indicators_month_type[year][month][action_type][objective] += 1

    indicators_month = sorted_dict_indicators_month(indicators_month)
    indicators_month_type = sorted_dict_indicators_month(indicators_month_type)
    indicators_year = sorted_dict_indicators_year(indicators_year)
    indicators_year_type = sorted_dict_indicators_year(indicators_year_type)

    return indicators_month, indicators_month_type, indicators_year, indicators_year_type

def get_qtd_actions_objectives_len(origin_database: dict) -> dict:
    indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        if "objetivos" in origin_database[code]:
            objectives = origin_database[code]["objetivos"]

            if year not in indicators_year: #Year
                indicators_year[year] = {}
                indicators_year_type[year] = {}

            if year not in indicators_month: #Year
                indicators_month[year] = {}
                indicators_month_type[year] = {}

            if month not in indicators_month[year]: #Month
                indicators_month[year][month] = {}
                indicators_month_type[year][month] = {}

            if action_type not in indicators_month[year]: #Action Type
                indicators_year_type[year][action_type] = {}

            if action_type not in indicators_month[year][month]: #Action Type
                indicators_month_type[year][month][action_type] = {}            

            if len(objectives) not in indicators_year[year]:
                indicators_year[year][len(objectives)] = 1
            else:       
                indicators_year[year][len(objectives)] += 1

            if len(objectives) not in indicators_year_type[year][action_type]:
                indicators_year_type[year][action_type][len(objectives)] = 1
            else:
                indicators_year_type[year][action_type][len(objectives)] += 1

            if len(objectives) not in indicators_month[year][month]:
                indicators_month[year][month][len(objectives)] = 1
            else:
                indicators_month[year][month][len(objectives)] += 1

            if len(objectives) not in indicators_month_type[year][month][action_type]:
                indicators_month_type[year][month][action_type][len(objectives)] = 1
            else:
                indicators_month_type[year][month][action_type][len(objectives)] += 1

    indicators_month = sorted_dict_indicators_month(indicators_month)
    indicators_month_type = sorted_dict_indicators_month(indicators_month_type)
    indicators_year = sorted_dict_indicators_year(indicators_year)
    indicators_year_type = sorted_dict_indicators_year(indicators_year_type)
                
    return indicators_month, indicators_month_type, indicators_year, indicators_year_type
