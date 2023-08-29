from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.dictionary_functions import *

def sorted_dict(dictionary: dict) -> dict:
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
                if year not in r_dictionary:
                    r_dictionary[year] = {}
                if month not in r_dictionary[year]:
                    r_dictionary[year][month] = {}
                r_dictionary[year][month][item] = dictionary[year][month][item]

    return r_dictionary

# def sorted_dict_info(dictionary: dict) -> dict:
#     r_dictionary = {}
#     for year in dictionary:
#         for action_type in dictionary[year]:
#             for month in sorted(dictionary[year][action_type], key=lambda x: list(DIGITS_MONTHS.values()).index(x)):
#                 if year not in r_dictionary:
#                     r_dictionary[year] = {}
#                 if action_type not in r_dictionary[year]:
#                     r_dictionary[year][action_type] = {}
#                 r_dictionary[year][action_type][month] = dictionary[year][action_type][month]
#     return r_dictionary

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

    return sorted_dict(indicators_month), sorted_dict_indicators_month(indicators_month_type), indicators_year, indicators_year_type

# def get_qtd_info_month_type_2(indicators: dict, origin_database: dict) -> dict:
#     for code in origin_database:
#         year = origin_database[code]["data_inicio"]["ano"]
#         digit_month = origin_database[code]["data_inicio"]["mes"]
#         month = DIGITS_MONTHS[digit_month]
#         action_type = origin_database[code]["tipo"]
#         status = origin_database[code]["situacao"]
#         convention_funpec = origin_database[code]["convenio_funpec"]
#         renovation = origin_database[code]["renovacao"]
#         proponent_unit = origin_database[code]["unidade_proponente"].split("/")[0].strip()
        
#         other_units = origin_database[code]["outras_unidades_envolvidas"]
#         if other_units == "":
#             other_units = ["Nenhuma"]
#         else:
#             other_units = other_units.split("\n")

#         main_area = origin_database[code]["area_principal"]
#         area_cnpq = origin_database[code]["area_do_cnpq"]
#         financial_source = origin_database[code]["fonte_de_financiamento"]
#         scholarships_requested = origin_database[code]["numero_bolsas_solicitadas"]
#         scholarships_obtained = origin_database[code]["numero_bolsas_concedidas"]
#         discents_involved = origin_database[code]["numero_discentes_envolvidos"]
        
#         if "faz_parte_de_programa_de_extensao" in origin_database[code]:
#             part_of_extension = origin_database[code]["faz_parte_de_programa_de_extensao"]
#         else:
#             part_of_extension = "NÃO"
            
#         public_estimated = return_number(origin_database[code]["publico_estimado"])
#         public_real = return_number(origin_database[code]["publico_real_atendido"])
    
#         if year not in indicators: #Year
#             indicators[year] = {}
#         if month not in indicators[year]:
#             indicators[year][month] = {}
#         if action_type not in indicators[year][month]:
#             indicators[year][month][action_type] = {}
#             # indicators[year][month][action_type]["qtd_convenio_funpec"] = 0
#             # indicators[year][month][action_type]["qtd_renovacao"] = 0
#             # indicators[year][month][action_type]["qtd_bolsas_solicitadas"] = 0
#             # indicators[year][month][action_type]["qtd_bolsas_concedidas"] = 0
#             # indicators[year][month][action_type]["qtd_discentes_envolvidos"] = 0
#             # indicators[year][month][action_type]["qtd_publico_estimado"] = 0
#             # indicators[year][month][action_type]["qtd_publico_real_atendido"] = 0
#             # indicators[year][month][action_type]["qtd_faz_parte_extensão"] = 0

#         if "situação" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["situação"] = {}
#         # if "proponente" not in indicators[year][month][action_type]:
#         #     indicators[year][month][action_type]["proponente"] = {}
#         # if "outras_unidades" not in indicators[year][month][action_type]:
#         #     indicators[year][month][action_type]["outras_unidades"] = {}
#         # if "area_principal" not in indicators[year][month][action_type]:
#         #     indicators[year][month][action_type]["area_principal"] = {}
#         # if "area_cnpq" not in indicators[year][month][action_type]:
#         #     indicators[year][month][action_type]["area_cnpq"] = {}
#         # if "fonte_financiamento" not in indicators[year][month][action_type]:
#         #     indicators[year][month][action_type]["fonte_financiamento"] = {}

        

       
#         if status not in indicators[year][month][action_type]["situação"]:
#             indicators[year][month][action_type]["situação"][status] = 1
#         else:
#             indicators[year][month][action_type]["situação"][status] += 1
        
#         # if proponent_unit not in indicators[year][month][action_type]["proponente"]:
#         #     indicators[year][month][action_type]["proponente"][proponent_unit] = 1
#         # else:
#         #     indicators[year][month][action_type]["proponente"][proponent_unit] += 1

#         # for unit in other_units:
#         #     if unit not in indicators[year][month][action_type]["outras_unidades"]:
#         #         indicators[year][month][action_type]["outras_unidades"][unit] = 1
#         #     else:
#         #         indicators[year][month][action_type]["outras_unidades"][unit] += 1

#         # if main_area not in indicators[year][month][action_type]["area_principal"]:
#         #     indicators[year][month][action_type]["area_principal"][main_area] = 1
#         # else:
#         #     indicators[year][month][action_type]["area_principal"][main_area] += 1

#         # if area_cnpq not in indicators[year][month][action_type]["area_cnpq"]:
#         #     indicators[year][month][action_type]["area_cnpq"][area_cnpq] = 1
#         # else:
#         #     indicators[year][month][action_type]["area_cnpq"][area_cnpq] += 1

#         # if financial_source not in indicators[year][month][action_type]["fonte_financiamento"]:
#         #     indicators[year][month][action_type]["fonte_financiamento"][financial_source] = 1
#         # else:
#         #     indicators[year][month][action_type]["fonte_financiamento"][financial_source] += 1
        
#         # if convention_funpec == "SIM":
#         #     indicators[year][month][action_type]["qtd_convenio_funpec"] += 1

#         # if renovation == "SIM":
#         #     indicators[year][month][action_type]["qtd_renovacao"] += 1

#         # if part_of_extension == "SIM":
#         #     indicators[year][month][action_type]["qtd_faz_parte_extensão"] += 1

#         # indicators[year][month][action_type]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
#         # indicators[year][month][action_type]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
#         # indicators[year][month][action_type]["qtd_discentes_envolvidos"] += int(discents_involved)
#         # indicators[year][month][action_type]["qtd_publico_estimado"] += int(public_estimated)
#         # indicators[year][month][action_type]["qtd_publico_real_atendido"] += int(public_real)
    
#     indicators = sorted_dict(indicators)     
#     return indicators