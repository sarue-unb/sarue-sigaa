# Specifics from extension page
import time
import components.selection_components as dc

def get_total_actions_indicator(driver):
    for year in range(2020, 2024): # 2020 to 2023
        _use_year(year, driver)
        make_search(driver)


def get_year_indicator(year: str, driver):
    _use_year(year, driver)
    make_search(driver)
    # Verificar se id = "painel-erros" está na página.
    # Se estiver, obter a quantidade por: A consulta retornou X resultados. Por favor, restrinja mais a busca.
    
    
    # Caso contrário, obter por:
    listing_count = dc.count_listing(driver)
    return f'Total of actions for the year of {year}: {listing_count}'

def get_action_by_year_indicator(year: str, action: str, driver):
    _use_year(year, driver)
    _use_type_action(action, driver)
    make_search(driver)
    listing_count = dc.count_listing(driver)
    return f'Total of {action} for the year of {year}: {listing_count}'

def make_search(driver):
    dc.use_element_by_id('formBuscaAtividade:btBuscar', driver)

def _use_year(year: int, driver):
    dc.use_element_by_id('formBuscaAtividade:selectBuscaAno', driver)
    dc.use_input_by_name('formBuscaAtividade:buscaAno', year, driver)
    
def _use_type_action(action: str, driver):
    tipoAcao = dc.get_element_by_select('formBuscaAtividade:buscaTipoAcao', 'CURSO', driver)
    time.sleep(10)
    # dc.use_element_by_value(1, tipoAcao)