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

def get_qtd_actions(indicators_month: dict, indicators_month_type: dict, indicators_year: dict, indicators_year_type: dict, origin_database: dict) -> dict:
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]

        # Year
        if year not in indicators_year: #Year
            indicators_year[year] = 1
        else:
            indicators_year[year] += 1

        # Month
        if year not in indicators_month: #Year
            indicators_month[year] = {}
        if month not in indicators_month[year]:
            indicators_month[year][month] = 1
        else:
            indicators_month[year][month] += 1

        # Year Type
        if year not in indicators_year_type: #Year
            indicators_year_type[year] = {}
        if action_type not in indicators_year_type[year]:
            indicators_year_type[year][action_type] = 1
        else:
            indicators_year_type[year][action_type] += 1

        # Month Type
        if year not in indicators_month_type: #Year
            indicators_month_type[year] = {}
        if month not in indicators_month_type[year]:
            indicators_month_type[year][month] = {}
        if action_type not in indicators_month_type[year][month]:
            indicators_month_type[year][month][action_type] = 1
        else:
            indicators_month_type[year][month][action_type] += 1

    indicators_month = sorted_dict(indicators_month)
    indicators_month_type = sorted_dict(indicators_month_type)

    return indicators_month, indicators_month_type, indicators_year, indicators_year_type

# def get_qtd_info_month_type(indicators: dict, origin_database: dict) -> dict:
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
#             indicators[year][month][action_type]["qtd_convenio_funpec"] = 0
#             indicators[year][month][action_type]["qtd_renovacao"] = 0
#             indicators[year][month][action_type]["qtd_bolsas_solicitadas"] = 0
#             indicators[year][month][action_type]["qtd_bolsas_concedidas"] = 0
#             indicators[year][month][action_type]["qtd_discentes_envolvidos"] = 0
#             indicators[year][month][action_type]["qtd_publico_estimado"] = 0
#             indicators[year][month][action_type]["qtd_publico_real_atendido"] = 0
#             indicators[year][month][action_type]["qtd_faz_parte_extensão"] = 0

#         if "situação" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["situação"] = {}
#         if "proponente" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["proponente"] = {}
#         if "outras_unidades" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["outras_unidades"] = {}
#         if "area_principal" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["area_principal"] = {}
#         if "area_cnpq" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["area_cnpq"] = {}
#         if "fonte_financiamento" not in indicators[year][month][action_type]:
#             indicators[year][month][action_type]["fonte_financiamento"] = {}

        

       
#         if status not in indicators[year][month][action_type]["situação"]:
#             indicators[year][month][action_type]["situação"][status] = 1
#         else:
#             indicators[year][month][action_type]["situação"][status] += 1
        
#         if proponent_unit not in indicators[year][month][action_type]["proponente"]:
#             indicators[year][month][action_type]["proponente"][proponent_unit] = 1
#         else:
#             indicators[year][month][action_type]["proponente"][proponent_unit] += 1

#         for unit in other_units:
#             if unit not in indicators[year][month][action_type]["outras_unidades"]:
#                 indicators[year][month][action_type]["outras_unidades"][unit] = 1
#             else:
#                 indicators[year][month][action_type]["outras_unidades"][unit] += 1

#         if main_area not in indicators[year][month][action_type]["area_principal"]:
#             indicators[year][month][action_type]["area_principal"][main_area] = 1
#         else:
#             indicators[year][month][action_type]["area_principal"][main_area] += 1

#         if area_cnpq not in indicators[year][month][action_type]["area_cnpq"]:
#             indicators[year][month][action_type]["area_cnpq"][area_cnpq] = 1
#         else:
#             indicators[year][month][action_type]["area_cnpq"][area_cnpq] += 1

#         if financial_source not in indicators[year][month][action_type]["fonte_financiamento"]:
#             indicators[year][month][action_type]["fonte_financiamento"][financial_source] = 1
#         else:
#             indicators[year][month][action_type]["fonte_financiamento"][financial_source] += 1
        
#         if convention_funpec == "SIM":
#             indicators[year][month][action_type]["qtd_convenio_funpec"] += 1

#         if renovation == "SIM":
#             indicators[year][month][action_type]["qtd_renovacao"] += 1

#         if part_of_extension == "SIM":
#             indicators[year][month][action_type]["qtd_faz_parte_extensão"] += 1

#         indicators[year][month][action_type]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
#         indicators[year][month][action_type]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
#         indicators[year][month][action_type]["qtd_discentes_envolvidos"] += int(discents_involved)
#         indicators[year][month][action_type]["qtd_publico_estimado"] += int(public_estimated)
#         indicators[year][month][action_type]["qtd_publico_real_atendido"] += int(public_real)
    
#     indicators = sorted_dict(indicators)     
#     return indicators

# def get_members_action(indicators: dict, origin_database: dict) -> dict:
# #     "sobre_publico" : {
# #       total : {
# #          discentes : X
# #          docentes : X
# #       }
# #       2020 : {
# #          discentes : X
# #          docentes : X
# #       }
# #       2020 : {
# #          janeiro : {
# #             discentes : X
# #             docentes : X
# #          }
# #       }
# #    }
    
#     for code in origin_database:
#         year = origin_database[code]["data_inicio"]["ano"]
#         digit_month = origin_database[code]["data_inicio"]["mes"]
#         month = DIGITS_MONTHS[digit_month]
#         action_type = origin_database[code]["tipo"]

#         if "membros_da_equipe" in origin_database[code]:
#             team_members = origin_database[code]["membros_da_equipe"]
        
#             if year not in indicators: #Year
#                 indicators[year] = {}
#             if month not in indicators[year]: #Month
#                 indicators[year][month] = {}
            
#             for member in team_members:
#                 name = member[0]
#                 role = member[1]

#                 if name not in indicators[year][month]:
#                     indicators[year][month][name] = {}
#                     indicators[year][month][name]["qtd"] = 1
#                     indicators[year][month][name]["papel"] = role
#                 else:
#                     indicators[year][month][name]["qtd"] += 1

#     return indicators

# def get_members_action_type(indicators: dict, origin_database: dict) -> dict:
#     for code in origin_database:
#         year = origin_database[code]["data_inicio"]["ano"]
#         digit_month = origin_database[code]["data_inicio"]["mes"]
#         month = DIGITS_MONTHS[digit_month]
#         action_type = origin_database[code]["tipo"]

#         if "membros_da_equipe" in origin_database[code]:
#             team_members = origin_database[code]["membros_da_equipe"]
        
#             if year not in indicators: #Year
#                 indicators[year] = {}
#             if month not in indicators[year]: #Month
#                 indicators[year][month] = {}
#             if action_type not in indicators[year][month]: #Action Type
#                 indicators[year][month][action_type] = {}
            
#             for member in team_members:
#                 name = member[0]
#                 role = member[1]

#                 if name not in indicators[year][month][action_type]:
#                     indicators[year][month][action_type][name] = {}
#                     indicators[year][month][action_type][name]["qtd"] = 1
#                     indicators[year][month][action_type][name]["papel"] = role
#                 else:
#                     indicators[year][month][action_type][name]["qtd"] += 1

#     return indicators

def return_number(text: str) -> int:
    padrao = r'(\d+)'
    resultado = re.search(padrao, text)  # Procurar o padrão no texto

    if resultado:
        return int(resultado.group(1))  # Converter o valor encontrado para um inteiro
    else:
        return 0
    