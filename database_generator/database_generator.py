import components.selection_components as sc
import components.info_printer as scif
import components.info_view as sciv
import database_generator.json_generator as jg
from config.output_format import *
from config.filter_descryption import *
from config.date_descryption import SPECIAL_DATE, FIRST_DAY_OF_MONTH, MONTHS_LAST_DAY

def get_every_extension_activity_from_months(start_month: int, end_month: int, year: int, offset:int, driver):
    if (end_month < start_month):
        print("ERROR: End Month less than start month")
        return
    
    for month in range(start_month, end_month + 1):
        if f'{month}/{year}' in SPECIAL_DATE:
            get_every_extension_activity_from_month_years_cnpq(month, year, offset, driver)
        else:
            get_every_extension_activity_from_month_years(month, year, offset, driver)

def get_every_extension_activity_from_month_years(month:int, year:int, offset:int, driver):
    _search_month_year(month, year, driver)

    qtd = sc.get_rows_len(driver) 

    if (qtd > offset): # maior que a quantidade quando não tem ações para discentes
        _get_activities_from_list_printer(driver, month, year)
        # _get_activities_from_list_view(driver, month, year)

def get_every_extension_activity_from_month_years_cnpq(month:str, year:str, offset:int, driver):
    for cnpq in AREA_CNPq:
        _search_month_year_cnpq(month, year, cnpq, driver)
        
        qtd = sc.get_rows_len(driver) 

        if (qtd > offset): # maior que a quantidade quando não tem ações para discentes
            _get_activities_from_list_printer(driver, month, year)
            # _get_activities_from_list_view(driver, month, year)

    _uncheck_cnpq(driver)

def get_every_extension_activity_from_month_years_passing_cnpq(month: str, year: str, cnpq:str, offset:int, driver):
    _search_month_year_cnpq(month, year, cnpq, driver)
    
    qtd = sc.get_rows_len(driver) 

    if (qtd > offset): # maior que a quantidade quando não tem ações para discentes
        _get_activities_from_list_printer(driver, month, year, cnpq)
        # _get_activities_from_list_view(driver, month,  year, cnpq)

    _uncheck_cnpq(driver)
        
def _get_activities_from_list_printer(driver, month:str, year:str, cnpq:str=None):
    activities_info = scif.get_row_data_printer(driver, month, year, cnpq)
    for row in activities_info:
        jg.add_item_to_crawler_database(row["codigo"], row)
        
def _get_activities_from_list_view(driver, month:str, year:str, cnpq:str=None):
    activities_info = sciv.get_row_data_view(driver, month, year)
    for row in activities_info:
        jg.add_item_to_crawler_database(row["codigo"], row)
        
def _search_month_year(month:int, year:int, driver):
    _clear_execution_period(driver)
    start_date = _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    sc.make_search(driver)
    
def _search_month_year_cnpq(month:int, year:int, cnpq:str, driver):
    _clear_execution_period(driver)
    start_date = _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    _use_type_action(cnpq, driver)
    sc.make_search(driver)
    
def _clear_execution_period(driver):
    sc.clear_input_name(NAME_DATA_INICIO_EXECUCAO, driver)
    sc.clear_input_name(NAME_DATA_FIM_EXECUCAO, driver)

def _use_execution_period(start_date:str, end_date:str, driver):
    sc.use_element_by_id(NAME_SELECT_BUSCAR_PERIODO, driver)
    sc.use_input_by_name(NAME_DATA_INICIO_EXECUCAO, start_date, driver)
    sc.use_input_by_name(NAME_DATA_FIM_EXECUCAO, end_date, driver)
    
def _use_type_action(cnpq:str, driver):
    sc.use_input_by_name(NAME_AREA_CNPq, cnpq, driver)

def _uncheck_cnpq(driver):
    sc.uncheck_checkbox_name(NAME_SELECT_AREA_CNPq, driver)

# def get_qtd_actions(start_year: str, end_year: str, driver:str):
#     if (end_year < start_year):
#         print("ERROR: End Year less than start year")
#         return
    
#     qtd = 0
#     for year in range(start_year, end_year + 1):
#         _clear_year(driver)
#         _use_year(year, driver)
       
#         # text = sc.get_error_message(driver)
#         # if text == None:
#         #     qtd += sc.count_listing(driver)
#         # else:   
#         #     qtd += int(text.split(" ")[3])  

#         if year == '2020':
#             qtd += sc.count_listing(driver)
#         else:
#             text = sc.get_error_message(driver)
#             qtd += int(text.split(" ")[3])  

#     _uncheck_year(driver)
#     return qtd

# def _clear_year(driver):
#     sc.clear_input_name(NAME_BUSCAR_ANO, driver)

# def _uncheck_year(driver):
#     sc.uncheck_checkbox_name(NAME_SELECT_BUSCAR_ANO, driver)

# def _use_year(year:str, driver):
#     sc.use_element_by_id(NAME_SELECT_BUSCAR_ANO, driver)
#     sc.use_input_by_name(NAME_BUSCAR_ANO, year, driver)
#     ep.make_search(driver)

def get_offset(month:int, year:int, driver):
    _search_month_year(month, year, driver)
    return sc.get_rows_len(driver) 

def _monthly_date_generator(month:int, year:int, monthEnd:bool) -> str:
    expetected_day = FIRST_DAY_OF_MONTH

    if monthEnd:
        expetected_day = MONTHS_LAST_DAY[month]

    # Sigaa does not accept single digit months
    if month < 10:
        month = '0' + str(month)

    #Sigaa automatically fills the slashes in the date
    return f'{expetected_day}{month}{year}'