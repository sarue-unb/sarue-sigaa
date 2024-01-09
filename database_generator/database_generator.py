# database_generator.py

## @file
# Módulo para gerar dados de extensão a partir do Sigaa.

import components.selection_components as sc
import components.info_printer as scif
import database_generator.json_generator as jg
from config.filter_descryption import *
from config.date_descryption import SPECIAL_DATE, FIRST_DAY_OF_MONTH, MONTHS_LAST_DAY, LEAP_YEAR

## Obtém todas as atividades de extensão de um conjunto de meses.
# @param start_month Mês inicial.
# @param end_month Mês final.
# @param year Ano.
# @param offset Deslocamento temporal.
# @param driver Objeto do driver do Selenium.
def get_every_extension_activity_from_months(start_month: int, end_month: int, year: int, offset:int, driver):
    if (end_month < start_month):
        print("ERROR: End Month less than start month")
        return
    
    for month in range(start_month, end_month + 1):
        if f'{month}/{year}' in SPECIAL_DATE:
            get_every_extension_activity_from_month_years_cnpq(month, year, offset, driver)
        else:
            get_every_extension_activity_from_month_years(month, year, offset, driver)

## Obtém todas as atividades de extensão de um mês específico.
# @param month Mês.
# @param year Ano.
# @param offset Deslocamento temporal.
# @param driver Objeto do driver do Selenium.
def get_every_extension_activity_from_month_years(month:int, year:int, offset:int, driver):
    _search_month_year(month, year, driver)

    qtd = sc.get_rows_len(driver) 

    if (qtd > offset): 
        _get_activities_from_list_printer(driver, month, year)

## Obtém todas as atividades de extensão de um mês específico para várias áreas CNPq.
# @param month Mês.
# @param year Ano.
# @param offset Deslocamento temporal.
# @param driver Objeto do driver do Selenium.
def get_every_extension_activity_from_month_years_cnpq(month:str, year:str, offset:int, driver):
    for cnpq in AREA_CNPq:
        _search_month_year_cnpq(month, year, cnpq, driver)
        
        qtd = sc.get_rows_len(driver) 

        if (qtd > offset): 
            _get_activities_from_list_printer(driver, month, year)
            
    _uncheck_cnpq(driver)

## Obtém todas as atividades de extensão de um mês específico para uma área CNPq específica.
# @param month Mês.
# @param year Ano.
# @param cnpq Área CNPq.
# @param offset Deslocamento temporal.
# @param driver Objeto do driver do Selenium.
def get_every_extension_activity_from_month_years_passing_cnpq(month: str, year: str, cnpq:str, offset:int, driver):
    _search_month_year_cnpq(month, year, cnpq, driver)
    
    qtd = sc.get_rows_len(driver) 

    if (qtd > offset): 
        _get_activities_from_list_printer(driver, month, year, cnpq)

    _uncheck_cnpq(driver)
        
## Obtém atividades de extensão a partir de uma lista utilizando a visualização de impressão.
# @param driver Objeto do driver do Selenium.
# @param month Mês.
# @param year Ano.
# @param cnpq Área CNPq (opcional).
def _get_activities_from_list_printer(driver, month:str, year:str, cnpq:str=None):
    activities_info = scif.get_row_data_printer(driver, month, year, cnpq)
    for row in activities_info:
        jg.add_item_to_crawler_database(row["codigo"], row)
        
## Realiza a busca por mês e ano.
# @param month Mês.
# @param year Ano.
# @param driver Objeto do driver do Selenium.
def _search_month_year(month:int, year:int, driver):
    _clear_execution_period(driver)
    start_date = _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    sc.make_search(driver)
    
## Realiza a busca por mês, ano e CNPq.
# @param month Mês.
# @param year Ano.
# @param cnpq Área CNPq.
# @param driver Objeto do driver do Selenium.
def _search_month_year_cnpq(month:int, year:int, cnpq:str, driver):
    _clear_execution_period(driver)
    start_date = _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    _use_type_action(cnpq, driver)
    sc.make_search(driver)
    
## Limpa o período de execução no formulário.
# @param driver Objeto do driver do Selenium.
def _clear_execution_period(driver):
    sc.clear_input_name(NAME_DATA_INICIO_EXECUCAO, driver)
    sc.clear_input_name(NAME_DATA_FIM_EXECUCAO, driver)

## Utiliza o período de execução no formulário.
# @param start_date Data de início.
# @param end_date Data de término.
# @param driver Objeto do driver do Selenium.
def _use_execution_period(start_date:str, end_date:str, driver):
    sc.use_element_by_id(NAME_SELECT_BUSCAR_PERIODO, driver)
    sc.use_input_by_name(NAME_DATA_INICIO_EXECUCAO, start_date, driver)
    sc.use_input_by_name(NAME_DATA_FIM_EXECUCAO, end_date, driver)
    
## Utiliza a área CNPq no formulário.
# @param cnpq Área CNPq.
# @param driver Objeto do driver do Selenium.
def _use_type_action(cnpq:str, driver):
    sc.use_input_by_name(NAME_AREA_CNPq, cnpq, driver)

## Desmarca a opção de área CNPq no formulário.
# @param driver Objeto do driver do Selenium.
def _uncheck_cnpq(driver):
    sc.uncheck_checkbox_name(NAME_SELECT_AREA_CNPq, driver)

## Obtém o deslocamento temporal a partir de um mês e ano.
# @param month Mês.
# @param year Ano.
# @param driver Objeto do driver do Selenium.
def get_offset(month:int, year:int, driver):
    _search_month_year(month, year, driver)
    return sc.get_rows_len(driver) 

## Gera a data mensal de acordo com o formato esperado pelo Sigaa.
# @param month Mês.
# @param year Ano.
# @param monthEnd Flag indicando se é o último dia do mês.
# @return String representando a data.
def _monthly_date_generator(month:int, year:int, monthEnd:bool) -> str:
    expetected_day = FIRST_DAY_OF_MONTH

    if monthEnd:
        if month == 2 and year in LEAP_YEAR:
            expetected_day = '29'
        else:
            expetected_day = MONTHS_LAST_DAY[month]

    if month < 10:
        month = '0' + str(month)

    return f'{expetected_day}{month}{year}'
