import components.selection_components as dc
from database_generator.constants import FIRST_DAY_OF_MONTH, MONTHS_LAST_DAY, ROWS_DATA_CELLS
import pages.extension_page as ep
import database_generator.json_generator as jg
from output_format import *

def get_every_extension_activity_from_years(start_year: str, end_year: str, driver, perfil:str):
    if (end_year < start_year):
        print("ERROR: End Year less than start year")
        return
    

    # ### Obter apenas 2020/5 na forma de discentes
    # year = 2020
    # month = 5

    # _search_month_year(month, year, driver)

    # qtd = dc.get_rows_len(driver) # 55 é a quantidade quando não tem ações para discentes

    # time = Timer()
    # time.set_start_time()

    # print(HASH, f'{month}/{year}', HASH)
    # if (qtd > 55):
    #     _get_activities_from_list_printer(driver)
    #     # _get_activities_from_list_view(driver)
    # print(f' {RIGHT_ARROW} Itens = {qtd-55} {LEFT_ARROW}')
    
    # time.print_partial_elapsed_ctime(f'{month}/{year}')  
    # ### REMOVER APOS TESTES

    for year in range(start_year, end_year + 1):
        for month in range(1,13): # Janeiro a Dezembro
            _search_month_year(month, year, driver)
            
            if perfil == "discente":
                qtd = dc.get_rows_len(driver) # 55 é a quantidade quando não tem ações para discentes

                time = Timer()
                time.set_start_time()

                print(HASH, f'{month}/{year}', HASH)
                if (qtd > 55):
                    _get_activities_from_list_printer(driver)
                    # _get_activities_from_list_view(driver)
                print(f' {RIGHT_ARROW} Itens = {qtd-55} {LEFT_ARROW}')
                
                time.print_partial_elapsed_ctime(f'{month}/{year}')  

            elif perfil == "docente":
                qtd = dc.count_listing(driver) # função demora muito quando não encontra

                if (qtd > 0):
                    _get_activities_from_list_printer(driver)
                    # _get_activities_from_list_view(driver)
    
    jg.generate_json()
    
def _get_activities_from_list_printer(driver):
    activities_info = dc.get_row_data_printer(driver)
    for row in activities_info:
        jg.add_item_to_database(row["codigo"], row)
        
def _get_activities_from_list_view(driver):
    activities_info = dc.get_row_data_view(driver)
    for row in activities_info:
        jg.add_item_to_database(row["codigo"], row)
        
def _search_month_year(month:int, year:int, driver):
    _clear_execution_period(driver)
    start_date =  _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    
def _clear_execution_period(driver):
    dc.clear_input('formBuscaAtividade:dataInicioExecucao', driver)
    dc.clear_input('formBuscaAtividade:dataFimExecucao', driver)

def _use_execution_period(start_date:str, end_date:str, driver):
    dc.use_element_by_id('formBuscaAtividade:selectBuscaPeriodoInicio', driver)
    dc.use_input_by_name('formBuscaAtividade:dataInicioExecucao', start_date, driver)
    dc.use_input_by_name('formBuscaAtividade:dataFimExecucao', end_date, driver)
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
