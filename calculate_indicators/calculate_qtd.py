# calculate_qtd.py
## @file
# Módulo para calcular todos os indicadores relacionados a qauntidade de ações.

from config.date_descryption import DIGITS_MONTHS
from calculate_indicators.sorted_dictionarys import *

def get_qtd_actions(origin_database: dict) -> dict:
    """
    Calculate the quantity of actions for each indicator in different time frames and types.

    This function takes an origin database as input and calculates the quantity of actions for each indicator in the
    following time frames and types: overall, yearly, monthly, yearly with action type, and monthly with action type.

    @param origin_database: Input database containing information about actions.
    @return: A tuple containing dictionaries for overall, yearly, monthly, yearly with action type, and monthly with
             action type indicators.
    """
    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}
    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]
           
        create_dictionary_place(indicators_month, year, {})
        create_dictionary_place(indicators_year_type, year, {})
        create_dictionary_place(indicators_month_type, year, {})

        create_dictionary_place(indicators_month_type[year], month, {})

        update_dictionary_place(indicators, action_type, 1)
        update_dictionary_place(indicators_year, year, 1)
        update_dictionary_place(indicators_month[year], month, 1)
        update_dictionary_place(indicators_year_type[year], action_type, 1)
        update_dictionary_place(indicators_month_type[year][month], action_type, 1)

    indicators_month = sorted_dict_year_month(indicators_month)
    indicators_month_type = sorted_dict_year_month(indicators_month_type)

    return indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type

def get_qtd_info(origin_database: dict) -> dict:
    """
    Calculate the quantity of information for each indicator in different time frames and types.

    This function takes an origin database as input and calculates the quantity of information for each indicator in
    the following time frames and types: overall, yearly, monthly, yearly with action type, and monthly with action type.

    @param origin_database: Input database containing information about actions.
    @return: A tuple containing dictionaries for overall, yearly, monthly, yearly with action type, and monthly with
             action type indicators.
    """
    indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type = {}, {}, {}, {}, {}

    indicators["qtd_convenio_funpec"] = 0
    indicators["qtd_renovacao"] = 0
    indicators["qtd_bolsas_solicitadas"] = 0
    indicators["qtd_bolsas_concedidas"] = 0
    indicators["qtd_discentes_envolvidos"] = 0
    indicators["qtd_publico_estimado"] = 0
    indicators["qtd_publico_real_atendido"] = 0
    indicators["qtd_faz_parte_extensão"] = 0

    for code in origin_database:
        year = origin_database[code]["data_inicio"]["ano"]
        digit_month = origin_database[code]["data_inicio"]["mes"]
        month = DIGITS_MONTHS[digit_month]
        action_type = origin_database[code]["tipo"]
        status = origin_database[code]["situacao"]
        convention_funpec = origin_database[code]["convenio_funpec"]
        renovation = origin_database[code]["renovacao"]
        proponent_unit = origin_database[code]["unidade_proponente"].split("/")[0].strip()
        

        other_units = origin_database[code]["outras_unidades_envolvidas"]
        if other_units == "":
            other_units = ["Nenhuma"]
        else:
            other_units = other_units.split("\n")

        main_area = origin_database[code]["area_principal"]
        area_cnpq = origin_database[code]["area_do_cnpq"]
        financial_source = origin_database[code]["fonte_de_financiamento"]
        scholarships_requested = origin_database[code]["numero_bolsas_solicitadas"]
        scholarships_obtained = origin_database[code]["numero_bolsas_concedidas"]
        discents_involved = return_number(origin_database[code]["numero_discentes_envolvidos"])
        
        if "faz_parte_de_programa_de_extensao" in origin_database[code]:
            part_of_extension = origin_database[code]["faz_parte_de_programa_de_extensao"]
        else:
            part_of_extension = "NÃO"
            
        public_estimated = return_number(origin_database[code]["publico_estimado"])
        public_real = return_number(origin_database[code]["publico_real_atendido"])
    
        # Year Type
        create_dictionary_place(indicators_year_type, year, {})

        # Month
        create_dictionary_place(indicators_month, year, {})
        
        # Month Type
        create_dictionary_place(indicators_month_type, year, {})
        create_dictionary_place(indicators_month_type[year], month, {})

        # Year
        if year not in indicators_year:
            indicators_year[year] = {}
            indicators_year[year]["qtd_convenio_funpec"] = 0
            indicators_year[year]["qtd_renovacao"] = 0
            indicators_year[year]["qtd_bolsas_solicitadas"] = 0
            indicators_year[year]["qtd_bolsas_concedidas"] = 0
            indicators_year[year]["qtd_discentes_envolvidos"] = 0
            indicators_year[year]["qtd_publico_estimado"] = 0
            indicators_year[year]["qtd_publico_real_atendido"] = 0
            indicators_year[year]["qtd_faz_parte_extensão"] = 0

        # Year Type
        if action_type not in indicators_year_type[year]:
            indicators_year_type[year][action_type] = {}
            indicators_year_type[year][action_type]["qtd_convenio_funpec"] = 0
            indicators_year_type[year][action_type]["qtd_renovacao"] = 0
            indicators_year_type[year][action_type]["qtd_bolsas_solicitadas"] = 0
            indicators_year_type[year][action_type]["qtd_bolsas_concedidas"] = 0
            indicators_year_type[year][action_type]["qtd_discentes_envolvidos"] = 0
            indicators_year_type[year][action_type]["qtd_publico_estimado"] = 0
            indicators_year_type[year][action_type]["qtd_publico_real_atendido"] = 0
            indicators_year_type[year][action_type]["qtd_faz_parte_extensão"] = 0

        # Month
        if month not in indicators_month[year]:
            indicators_month[year][month] = {}
            indicators_month[year][month]["qtd_convenio_funpec"] = 0
            indicators_month[year][month]["qtd_renovacao"] = 0
            indicators_month[year][month]["qtd_bolsas_solicitadas"] = 0
            indicators_month[year][month]["qtd_bolsas_concedidas"] = 0
            indicators_month[year][month]["qtd_discentes_envolvidos"] = 0
            indicators_month[year][month]["qtd_publico_estimado"] = 0
            indicators_month[year][month]["qtd_publico_real_atendido"] = 0
            indicators_month[year][month]["qtd_faz_parte_extensão"] = 0

        # Month Type
        if action_type not in indicators_month_type[year][month]:
            indicators_month_type[year][month][action_type] = {}
            indicators_month_type[year][month][action_type]["qtd_convenio_funpec"] = 0
            indicators_month_type[year][month][action_type]["qtd_renovacao"] = 0
            indicators_month_type[year][month][action_type]["qtd_bolsas_solicitadas"] = 0
            indicators_month_type[year][month][action_type]["qtd_bolsas_concedidas"] = 0
            indicators_month_type[year][month][action_type]["qtd_discentes_envolvidos"] = 0
            indicators_month_type[year][month][action_type]["qtd_publico_estimado"] = 0
            indicators_month_type[year][month][action_type]["qtd_publico_real_atendido"] = 0
            indicators_month_type[year][month][action_type]["qtd_faz_parte_extensão"] = 0

        # Full
        create_dictionary_place(indicators, "situação", {})
        create_dictionary_place(indicators, "proponente", {})
        create_dictionary_place(indicators, "outras_unidades", {})
        create_dictionary_place(indicators, "area_principal", {})
        create_dictionary_place(indicators, "area_cnpq", {})
        create_dictionary_place(indicators, "fonte_financiamento", {})

        # Year
        create_dictionary_place(indicators_year[year], "situação", {})
        create_dictionary_place(indicators_year[year], "proponente", {})
        create_dictionary_place(indicators_year[year], "outras_unidades", {})
        create_dictionary_place(indicators_year[year], "area_principal", {})
        create_dictionary_place(indicators_year[year], "area_cnpq", {})
        create_dictionary_place(indicators_year[year], "fonte_financiamento", {})

        # Year Type
        create_dictionary_place(indicators_year_type[year][action_type], "situação", {})
        create_dictionary_place(indicators_year_type[year][action_type], "proponente", {})
        create_dictionary_place(indicators_year_type[year][action_type], "outras_unidades", {})
        create_dictionary_place(indicators_year_type[year][action_type], "area_principal", {})
        create_dictionary_place(indicators_year_type[year][action_type], "area_cnpq", {})
        create_dictionary_place(indicators_year_type[year][action_type], "fonte_financiamento", {})
        
        # Month
        create_dictionary_place(indicators_month[year][month], "situação", {})
        create_dictionary_place(indicators_month[year][month], "proponente", {})
        create_dictionary_place(indicators_month[year][month], "outras_unidades", {})
        create_dictionary_place(indicators_month[year][month], "area_principal", {})
        create_dictionary_place(indicators_month[year][month], "area_cnpq", {})
        create_dictionary_place(indicators_month[year][month], "fonte_financiamento", {})

        # Month Type
        create_dictionary_place(indicators_month_type[year][month][action_type], "situação", {})
        create_dictionary_place(indicators_month_type[year][month][action_type], "proponente", {})
        create_dictionary_place(indicators_month_type[year][month][action_type], "outras_unidades", {})
        create_dictionary_place(indicators_month_type[year][month][action_type], "area_principal", {})
        create_dictionary_place(indicators_month_type[year][month][action_type], "area_cnpq", {})
        create_dictionary_place(indicators_month_type[year][month][action_type], "fonte_financiamento", {})

        # Full
        update_dictionary_place(indicators["situação"], status, 1)
        update_dictionary_place(indicators["proponente"], proponent_unit, 1)

        for unit in other_units:
            update_dictionary_place(indicators["outras_unidades"], unit, 1)

        update_dictionary_place(indicators["area_principal"], main_area, 1)
        update_dictionary_place(indicators["area_cnpq"], area_cnpq, 1)
        update_dictionary_place(indicators["fonte_financiamento"], financial_source, 1)

        indicators["qtd_convenio_funpec"] += 1 if convention_funpec == "SIM" else 0
        indicators["qtd_renovacao"] += 1 if renovation == "SIM" else 0
        indicators["qtd_faz_parte_extensão"] += 1 if part_of_extension == "SIM" else 0

        indicators["qtd_bolsas_solicitadas"] += int(scholarships_requested)
        indicators["qtd_bolsas_concedidas"] += int(scholarships_obtained)
        indicators["qtd_discentes_envolvidos"] += int(discents_involved)
        indicators["qtd_publico_estimado"] += int(public_estimated)
        indicators["qtd_publico_real_atendido"] += int(public_real)

        # Year
        update_dictionary_place(indicators_year[year]["situação"], status, 1)
        update_dictionary_place(indicators_year[year]["proponente"], proponent_unit, 1)
        
        for unit in other_units:
            update_dictionary_place(indicators_year[year]["outras_unidades"], unit, 1)

        update_dictionary_place(indicators_year[year]["area_principal"], main_area, 1)
        update_dictionary_place(indicators_year[year]["area_cnpq"], area_cnpq, 1)
        update_dictionary_place(indicators_year[year]["fonte_financiamento"], financial_source, 1)

        indicators_year[year]["qtd_convenio_funpec"] += 1 if convention_funpec == "SIM" else 0
        indicators_year[year]["qtd_renovacao"] += 1 if renovation == "SIM" else 0
        indicators_year[year]["qtd_faz_parte_extensão"] += 1 if part_of_extension == "SIM" else 0

        indicators_year[year]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
        indicators_year[year]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
        indicators_year[year]["qtd_discentes_envolvidos"] += int(discents_involved)
        indicators_year[year]["qtd_publico_estimado"] += int(public_estimated)
        indicators_year[year]["qtd_publico_real_atendido"] += int(public_real)

        # Year Type
        update_dictionary_place(indicators_year_type[year][action_type]["situação"], status, 1)
        update_dictionary_place(indicators_year_type[year][action_type]["proponente"], proponent_unit, 1)

        for unit in other_units:
            update_dictionary_place(indicators_year_type[year][action_type]["outras_unidades"], unit, 1)

        update_dictionary_place(indicators_year_type[year][action_type]["area_principal"], main_area, 1)
        update_dictionary_place(indicators_year_type[year][action_type]["area_cnpq"], area_cnpq, 1)
        update_dictionary_place(indicators_year_type[year][action_type]["fonte_financiamento"], financial_source, 1)

        indicators_year_type[year][action_type]["qtd_convenio_funpec"] += 1 if convention_funpec == "SIM" else 0
        indicators_year_type[year][action_type]["qtd_renovacao"] += 1 if renovation == "SIM" else 0
        indicators_year_type[year][action_type]["qtd_faz_parte_extensão"] += 1 if part_of_extension == "SIM" else 0

        indicators_year_type[year][action_type]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
        indicators_year_type[year][action_type]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
        indicators_year_type[year][action_type]["qtd_discentes_envolvidos"] += int(discents_involved)
        indicators_year_type[year][action_type]["qtd_publico_estimado"] += int(public_estimated)
        indicators_year_type[year][action_type]["qtd_publico_real_atendido"] += int(public_real)
        
        # Month
        update_dictionary_place(indicators_month[year][month]["situação"], status, 1)
        update_dictionary_place(indicators_month[year][month]["proponente"], proponent_unit, 1)

        for unit in other_units:
            update_dictionary_place(indicators_month[year][month]["outras_unidades"], unit, 1)

        update_dictionary_place(indicators_month[year][month]["area_principal"], main_area, 1)
        update_dictionary_place(indicators_month[year][month]["area_cnpq"], area_cnpq, 1)
        update_dictionary_place(indicators_month[year][month]["fonte_financiamento"], financial_source, 1)

        indicators_month[year][month]["qtd_convenio_funpec"] += 1 if convention_funpec == "SIM" else 0
        indicators_month[year][month]["qtd_renovacao"] += 1 if renovation == "SIM" else 0
        indicators_month[year][month]["qtd_faz_parte_extensão"] += 1 if part_of_extension == "SIM" else 0

        indicators_month[year][month]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
        indicators_month[year][month]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
        indicators_month[year][month]["qtd_discentes_envolvidos"] += int(discents_involved)
        indicators_month[year][month]["qtd_publico_estimado"] += int(public_estimated)
        indicators_month[year][month]["qtd_publico_real_atendido"] += int(public_real)

        # Month Type
        update_dictionary_place(indicators_month_type[year][month][action_type]["situação"], status, 1)
        update_dictionary_place(indicators_month_type[year][month][action_type]["proponente"], proponent_unit, 1)

        for unit in other_units:
            update_dictionary_place(indicators_month_type[year][month][action_type]["outras_unidades"], unit, 1)
        
        update_dictionary_place(indicators_month_type[year][month][action_type]["area_principal"], main_area, 1)
        update_dictionary_place(indicators_month_type[year][month][action_type]["area_cnpq"], area_cnpq, 1)
        update_dictionary_place(indicators_month_type[year][month][action_type]["fonte_financiamento"], financial_source, 1)

        indicators_month_type[year][month][action_type]["qtd_convenio_funpec"] += 1 if convention_funpec == "SIM" else 0
        indicators_month_type[year][month][action_type]["qtd_renovacao"] += 1 if renovation == "SIM" else 0
        indicators_month_type[year][month][action_type]["qtd_faz_parte_extensão"] += 1 if part_of_extension == "SIM" else 0

        indicators_month_type[year][month][action_type]["qtd_bolsas_solicitadas"] += int(scholarships_requested)
        indicators_month_type[year][month][action_type]["qtd_bolsas_concedidas"] += int(scholarships_obtained)
        indicators_month_type[year][month][action_type]["qtd_discentes_envolvidos"] += int(discents_involved)
        indicators_month_type[year][month][action_type]["qtd_publico_estimado"] += int(public_estimated)
        indicators_month_type[year][month][action_type]["qtd_publico_real_atendido"] += int(public_real)
    
    indicators_month = sorted_dict_year_month(indicators_month)
    indicators_month_type = sorted_dict_year_month(indicators_month_type)     
    indicators_year_type =sorted_dict_indicators_year(indicators_year_type)
    return indicators, indicators_month, indicators_month_type, indicators_year, indicators_year_type