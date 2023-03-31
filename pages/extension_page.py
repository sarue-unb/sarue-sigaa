# Specifics from extension page
import components.selection_components as dc

def get_year_indicator(year: str, driver):
    _use_year(year, driver)
    _make_search(driver)
    listing_count = dc.count_listing(driver)
    return f'Total of actions for the year of {year}: {listing_count}'

def _use_year(year: int, driver):
    dc.use_element_by_id('formBuscaAtividade:selectBuscaAno', driver)
    dc.use_input_by_name('formBuscaAtividade:buscaAno', year, driver)
    
def _make_search(driver):
    dc.use_element_by_id('formBuscaAtividade:btBuscar', driver)
