from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from database_generator.constants import *
from output_format import SIZE_TERMINAL
import components.info_printer as Printer
from tqdm import tqdm

def get_error_message(driver):
    try:
        return driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/ul/li').text
    except:
        return None
    
def use_input_by_name(name: str, input: str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.click()
    input_field.send_keys(input)
    
def clear_input(name: str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.clear()
    
def uncheck_checkbox(name: str, driver):
    checkbox = driver.find_element(By.NAME, name)
    if checkbox.is_selected():
        checkbox.click()
        
def use_element_by_id(id: str, driver):
    driver.find_element(By.ID, id).click()

def use_element_by_xpath(value: int, driver):
    return driver.find_element(By.XPATH, value).click()

def use_element_by_class(class_name: str, driver):
    driver.find_element(By.CLASS_NAME, class_name).click()

def get_element_by_id(id: str, driver):
    return driver.find_element(By.ID, id)

def get_element_by_xpath(value: int, driver):
    return driver.find_element(By.XPATH, value)

def get_element_by_class(class_name: str, driver):
    driver.find_element(By.CLASS_NAME, class_name)

def get_element_by_select(name: str, option: str, driver):
    select = Select(driver.find_element_by_name(name))
    select.select_by_visible_text(option)

def count_listing(driver):
    try:
        # This is being done directly through XPATH
        # But we could also do it by using the table Id
        rows = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/form[2]/table/tbody/tr')
        return len(rows)
    except:
        return 0
    
def get_rows_len(result_table):
     return len(result_table.find_elements(By.XPATH, ".//tr"))

def get_rows_from_table(driver):
        return driver.find_element(By.ID, "listagem")

def get_row_data_printer(driver, month, year):
    rows_total_data = []
    result_table = get_rows_from_table(driver)
    rows_length = get_rows_len(result_table)

    desc = f'{month:02d}/{year}'
    for i in tqdm(range(0, rows_length - 1), desc=desc, bar_format='{desc} - {elapsed} {bar} {n_fmt}/{total_fmt} - {percentage:.0f}%', ncols=SIZE_TERMINAL): # tqdm is a progress bar
        use_element_by_id(PRINTER_FORM_ID_PRE_FIX + str(i) + PRINTER_FORM_ID_POS_FIX, result_table)
        
        row_info = Printer.get_info_from_print_page(driver)
        add_date_to_item(row_info, month, year)
        rows_total_data.append(row_info)
        
        use_element_by_class("voltar", driver)
        # use_element_by_xpath("/html/body/div/div[4]/p/table/tbody/tr/td[1]", driver) # Does not work, voltar element can also be found in the table /html/body/div/div[2]/p/table/tbody/tr/td[1]

        result_table = get_rows_from_table(driver)
        
    return rows_total_data

def get_row_data_view(driver, month, year):
    rows_total_data = []
    result_table = get_rows_from_table(driver)
    rows_length = get_rows_len(result_table)
    
    for i in tqdm(range(0, rows_length - 1)): # tqdm is a progress bar
        use_element_by_id(VIEW_FORM_ID_PRE_FIX + str(i) + VIEW_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_view_page(driver)
        add_date_to_item(row_info, month, year)
        rows_total_data.append(row_info)
        
        use_element_by_class("voltar", driver)
        # use_element_by_xpath("/html/body/div[2]/div[2]/form/table/tfoot/tr/td/input", driver)

        result_table = get_rows_from_table(driver)
        
    return rows_total_data

def add_date_to_item(item, month, year):
     item['data_inicio'] = {'mes': month, 'ano': year}
     return item

def get_info_try_except(xpath, driver):
    try:
        return get_element_by_xpath(xpath, driver).text
    except:
        return "N/A"
    
def get_info_direct(xpath, driver):
    return get_element_by_xpath(xpath, driver).text

def get_info_from_view_page(driver):
    info = {}

    info["codigo"] = get_info_direct("//html/body/div[2]/div[2]/form/table/tbody/tr[2]/td", driver)
    info["titulo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver)

    info["categoria"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td[1]", driver)
    info["abrangencia"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td[2]", driver)
    info["ano"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[1]", driver)
    info["periodo_realizacao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]", driver)

    info["unidade_proponente"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[6]/td", driver)  
    info["unidade_orcamentaria"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[7]/td", driver)
    info["executor_financeiro"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[8]/td", driver)
    info["unidade_coexecutora"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[9]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[10]/td", driver)

    info["area_cnpq"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[11]/td[1]", driver)
    info["area_principal"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[11]/td[2]", driver)
    info["qtd_bolsas_solicitadas"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[12]/td[1]", driver)
    info["qtd_bolsas_concedidas"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[12]/td[2]", driver)
    info["tipo_cadastro"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[1]", driver)
    info["convenio_funpec"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]", driver)
    info["publico_alvo_interno"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[14]/td[1]", driver)
    info["publico_alvo_externo"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[14]/td[2]", driver)
    info["publico_estimado_externo"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[15]/td[1]", driver)
    info["publico_estimado_interno"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[15]/td[2]", driver)

    info["publico_real_atingido"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[16]/td", driver)
    
    info["fonte_financiamento"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td[1]", driver)
    info["renovacao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td[2]", driver)

    info["linha_atuacao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td", driver)
    info["programa_estrategico"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[19]/td", driver)
    info["vinculado_acao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[20]/td", driver)
    info["vinculado_grupo"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[21]/td", driver)
    info["parte_programa_extensao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[22]/td", driver)
    info["tipo_evento"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[24]/td", driver)
    info["periodo_evento"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[25]/td", driver)

    if(info["categoria"] == "EVENTO" or info["categoria"] == "CURSO"):
        info["carga_horaria"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[26]/td[1]", driver)
        info["previsao_vagas"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[26]/td[2]", driver)

    info["situacao"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[27]/td", driver)
    info["reponsavel_acao_nome"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[28]/td", driver)
    info["reponsavel_acao_email"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[29]/td", driver)
    info["reponsavel_acao_telefone"] = get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[30]/td", driver)

    # info["estado_realizacao"] = get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[1]")
    # info["municipio_realizacao"] = get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[2]", driver)
    # info["bairro_realizacao"] = get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[3]", driver)
    # info["espaco_realizacao"] = get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[4]", driver)

    # Aqui precisa ter paciencia, ate fazer uma função para verificar se a imagem contida é light ou não

    return info