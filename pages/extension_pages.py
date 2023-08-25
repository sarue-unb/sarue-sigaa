# Specifics from extension page
import components.selection_components as sc
from config.filter_descryption import *

# def make_search(driver):
#     sc.use_element_by_id(NAME_BUTTON_BUSCAR, driver)

# def get_year_indicator(year: str, driver):
#     _use_year(year, driver)
#     make_search(driver)
#     # Verificar se id = "painel-erros" está na página.
#     # Se estiver, obter a quantidade por: A consulta retornou X resultados. Por favor, restrinja mais a busca.
    
    
#     # Caso contrário, obter por:
#     listing_count = sc.count_listing(driver)
#     return f'Total of actions for the year of {year}: {listing_count}'

# def get_action_by_year_indicator(year: str, action: str, driver):
#     _use_year(year, driver)
#     _use_type_action(action, driver)
#     make_search(driver)
#     listing_count = sc.count_listing(driver)
#     return f'Total of {action} for the year of {year}: {listing_count}'

# def _use_year(year: int, driver):
#     sc.use_element_by_id(NAME_SELECT_BUSCAR_ANO, driver)
#     sc.use_input_by_name(NAME_BUSCAR_ANO, year, driver)
    
# def _use_type_action(action: str, driver):
#     tipoAcao = sc.get_element_by_select('formBuscaAtividade:buscaTipoAcao', 'CURSO', driver)
#     # dc.use_element_by_value(1, tipoAcao)