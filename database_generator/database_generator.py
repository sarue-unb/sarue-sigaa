import components.selection_components as sc
from database_generator.constants import FIRST_DAY_OF_MONTH, MONTHS_LAST_DAY, ROWS_DATA_CELLS
import pages.extension_page as ep
import database_generator.json_generator as jg
from output_format import *
    
def get_every_extension_activity_from_years(start_year: str, end_year: str, driver:str, perfil:str):
    if (end_year < start_year):
        print("ERROR: End Year less than start year")
        return
    
    for year in range(start_year, end_year + 1):
        time = Timer()
        time.set_start_time()
        for month in range(1,13): # Janeiro a Dezembro
            _search_month_year(month, year, driver)
            
            if perfil == "discente":
                qtd = sc.get_rows_len(driver) # 55 é a quantidade quando não tem ações para discentes

                if (qtd > 55):
                    _get_activities_from_list_printer(driver, month, year)
                    # _get_activities_from_list_view(driver, month, year)
                    
            elif perfil == "docente":
                qtd = sc.count_listing(driver) # função demora muito quando não encontra

                if (qtd > 0):
                    _get_activities_from_list_printer(driver, month, year)
                    # _get_activities_from_list_view(driver, month, year)
    
        time.print_partial_elapsed_ctime(f'{year}')  
                    
    jg.generate_json(start_year, end_year)

def get_every_extension_activity_from_month_years(month: str, year: str, driver, perfil:str):
    _search_month_year(month, year, driver)

    if perfil == "discente":
        qtd = sc.get_rows_len(driver) # 55 é a quantidade quando não tem ações para discentes

        if (qtd > 55):
            _get_activities_from_list_printer(driver, month, year)
            # _get_activities_from_list_view(driver, month, year)

    jg.generate_json(year, year)
        
def _get_activities_from_list_printer(driver, month, year):
    activities_info = sc.get_row_data_printer(driver, month, year)
    for row in activities_info:
        jg.add_item_to_database(row["codigo"], row)
        
def _get_activities_from_list_view(driver, month, year):
    activities_info = sc.get_row_data_view(driver, month, year)
    for row in activities_info:
        jg.add_item_to_database(row["codigo"], row)
        
def _search_month_year(month:int, year:int, driver):
    _clear_execution_period(driver)
    start_date =  _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    
def _clear_execution_period(driver):
    sc.clear_input('formBuscaAtividade:dataInicioExecucao', driver)
    sc.clear_input('formBuscaAtividade:dataFimExecucao', driver)

def _use_execution_period(start_date:str, end_date:str, driver):
    sc.use_element_by_id('formBuscaAtividade:selectBuscaPeriodoInicio', driver)
    sc.use_input_by_name('formBuscaAtividade:dataInicioExecucao', start_date, driver)
    sc.use_input_by_name('formBuscaAtividade:dataFimExecucao', end_date, driver)
    ep.make_search(driver)

def get_qtd_actions(start_year: str, end_year: str, driver:str):
    if (end_year < start_year):
        print("ERROR: End Year less than start year")
        return
    
    qtd = 0
    for year in range(start_year, end_year + 1):
        _clear_year(driver)
        _use_year(year, driver)
       
        # text = sc.get_error_message(driver)
        # if text == None:
        #     qtd += sc.count_listing(driver)
        # else:   
        #     qtd += int(text.split(" ")[3])  

        if year == '2020':
            qtd += sc.count_listing(driver)
        else:
            text = sc.get_error_message(driver)
            qtd += int(text.split(" ")[3])  

    _uncheck_year(driver)
    return qtd

def _clear_year(driver):
    sc.clear_input('formBuscaAtividade:buscaAno', driver)

def _uncheck_year(driver):
    sc.uncheck_checkbox('formBuscaAtividade:selectBuscaAno', driver)

def _use_year(year:str, driver):
    sc.use_element_by_id('formBuscaAtividade:selectBuscaAno', driver)
    sc.use_input_by_name('formBuscaAtividade:buscaAno', year, driver)
    ep.make_search(driver)

def _monthly_date_generator(month:int, year:int, monthEnd:bool) -> str:
    expetected_day = FIRST_DAY_OF_MONTH

    if monthEnd:
        expetected_day = MONTHS_LAST_DAY[month]

    # Sigaa does not accept single digit months
    if month < 10:
        month = '0' + str(month)

    #Sigaa automatically fills the slashes in the date
    return f'{expetected_day}{month}{year}'