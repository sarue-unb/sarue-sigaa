import components.selection_components as dc
from database_generator.constants import FIRST_DAY_OF_MONTH, MONTHS_LAST_DAY, ROWS_DATA_CELLS
import pages.extension_page as ep
import database_generator.json_generator as jg
from output_format import *

def get_every_extension_activity_from_years(start_year: str, end_year: str, driver):
    if (end_year < start_year):
        print("ERROR: End Year less than start year")
        return
    
    for year in range(start_year, end_year + 1):
        for month in range(1,13): # Janeiro a Dezembro
            _search_month_year(month, year, driver)
            
            print(RIGHT_ARROW, year, month, HASH, dc.count_listing(driver), LEFT_ARROW)
            if (dc.count_listing(driver) != 0):
                _get_activities_from_list(driver)
    
    jg.generate_json()
    
def _get_activities_from_list(driver):
    list_table = dc.get_tbody_rows_from_table(driver)
    for row in list_table:
        print("Adding row: now", row)
        activity = {}
        codigo = dc.get_data_cells_from_from_rows(ROWS_DATA_CELLS["codigo"], row)
        activity["titulo"] = dc.get_data_cells_from_from_rows(ROWS_DATA_CELLS["titulo"], row)
        activity["unidade"] = dc.get_data_cells_from_from_rows(ROWS_DATA_CELLS["unidade"], row)
        activity["situacao"] = dc.get_data_cells_from_from_rows(ROWS_DATA_CELLS["situacao"], row)
        activity["dimensao_academica "] = dc.get_data_cells_from_from_rows(ROWS_DATA_CELLS["dimensao_academica"], row)
        jg.add_item_to_database(codigo, activity)
        
def _search_month_year(month:int, year:int, driver):
    _clear_execution_period(driver)
    start_date =  _monthly_date_generator(month, year, False)
    end_date = _monthly_date_generator(month, year, True)
    _use_execution_period(start_date, end_date, driver)
    

def _clear_execution_period(driver):
    print("Clearing input")
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
