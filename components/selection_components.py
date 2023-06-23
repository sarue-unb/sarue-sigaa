from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from database_generator.constants import *
from tqdm import tqdm

def use_input_by_name(name: str, input: str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.click()
    input_field.send_keys(input)
    
def clear_input(name: str, driver):
    input_field = driver.find_element(By.NAME, name)
    input_field.clear()
    
def use_element_by_id(id: str, driver):
    driver.find_element(By.ID, id).click()

def use_element_by_class(class_name: str, driver):
    driver.find_element(By.CLASS_NAME, class_name).click()

def use_element_by_xpath(value: int, driver):
    return driver.find_element(By.XPATH, value).click()

def get_element_by_xpath(value: int, driver):
    return driver.find_element(By.XPATH, value)

def get_element_by_id(id: str, driver):
    return driver.find_element(By.ID, id)

def get_element_by_select(name: str, option: str, driver):
    select = Select(driver.find_element_by_name(name))
    select.select_by_visible_text(option)

def get_element_by_class(class_name: str, driver):
    driver.find_element(By.CLASS_NAME, class_name)

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

def get_row_data_printer( driver):
    rows_total_data = []
    result_table = get_rows_from_table(driver)
    rows_length = get_rows_len(result_table)
    
    for i in tqdm(range(0, rows_length - 1)): # tqdm is a progress bar
        use_element_by_id(PRINTER_FORM_ID_PRE_FIX + str(i) + PRINTER_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_print_page(driver)
        rows_total_data.append(row_info)
        
        # use_element_by_class("voltar", driver)
        use_element_by_xpath("/html/body/div/div[4]/p/table/tbody/tr/td[1]", driver)

        result_table = get_rows_from_table(driver)
        
    return rows_total_data

def get_row_data_view( driver):
    rows_total_data = []
    result_table = get_rows_from_table(driver)
    rows_length = get_rows_len(result_table)
    
    for i in tqdm(range(0, rows_length - 1)): # tqdm is a progress bar
        use_element_by_id(VIEW_FORM_ID_PRE_FIX + str(i) + VIEW_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_view_page(driver)
        rows_total_data.append(row_info)
        
        # use_element_by_class("voltar", driver)
        use_element_by_xpath("/html/body/div[2]/div[2]/form/table/tfoot/tr/td/input", driver)

        result_table = get_rows_from_table(driver)
        
    return rows_total_data

def get_info_try_except(xpath, driver):
    try:
        return get_element_by_xpath(xpath, driver).text
    except:
        return "N/A"
    
def get_info_direct(xpath, driver):
    return get_element_by_xpath(xpath, driver).text
    
def get_info_from_print_page(driver):
    info = {}

    info["codigo"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td", driver)
    info["titulo"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td", driver)
    info["ano"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver)
    info["periodo_de_realizacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td", driver)
    info["tipo"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td", driver)
    info["situacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td", driver)
    info["munincipio_de_realizacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    #This is a table, contrary to the other fields
    # info["outras_unidades_envolvidas"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["publico_estimado"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_real_atendido"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["tipo_de_cadastro"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["tipo_do_evento"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["periodo_do_evento"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["carga_horario"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["previsao_n_de_vagas"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)
    info["contato_coordenacao"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[31]/td", driver)
    info["contato_email"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver)
    info["contato_telefone"] = get_info_try_except("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver)
    
    return info

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

# def get_info_from_print_page(driver):
#     info = {}
#     try:
#         info["codigo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td", driver).text
#     except:
#         info["codigo"] = "N/A"
#     try:
#         info["titulo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td", driver).text
#     except:
#         info["titulo"] = "N/A"
#     try:
#         info["ano"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver).text
#     except:
#         info["ano"] = "N/A"
#     try:
#         info["periodo_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td", driver).text
#     except:
#         info["periodo_de_realizacao"] = "N/A"
#     try:
#         info["tipo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td", driver).text
#     except:
#         info["tipo"] = "N/A"
#     try:
#         info["situacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td", driver).text
#     except:
#         info["situacao"] = "N/A"
#     try:
#         info["munincipio_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver).text
#     except:
#         info["munincipio_de_realizacao"] = "N/A"
#     try:
#         info["espaco_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver).text
#     except:
#         info["espaco_de_realizacao"] = "N/A"
#     try:
#         info["abrangencia"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver).text
#     except:
#         info["abrangencia"] = "N/A"
#     try:
#         info["publico_alvo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver).text
#     except:
#         info["publico_alvo"] = "N/A"
#     try:
#         info["unidade_proponente"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver).text
#     except:
#         info["unidade_proponente"] = "N/A"
#     try:
#         info["unidade_orcamentaria"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver).text
#     except:
#         info["unidade_orcamentaria"] = "N/A"

#     # try:
#     #     #This is a table, contrary to the other fields
#     #     info["outras_unidades_envolvidas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td/table/tbody/tr/td", driver).text
#     # except:
#     #     info["outras_unidades_envolvidas"] = "N/A"
#     try:
#         info["area_principal"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver).text
#     except:
#         info["area_principal"] = "N/A"
#     try:
#         info["area_do_cnpq"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver).text
#     except:
#         info["area_do_cnpq"] = "N/A"
#     try:
#         info["fonte_de_financiamento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver).text
#     except:
#         info["fonte_de_financiamento"] = "N/A"
#     try:
#         info["convenio_funpec"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver).text
#     except:
#         info["convenio_funpec"] = "N/A"
#     try:
#         info["renovacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver).text
#     except:
#         info["renovacao"] = "N/A"
#     try:
#         info["numero_bolsas_solicitadas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver).text
#     except:
#         info["numero_bolsas_solicitadas"] = "N/A"
#     try:
#         info["numero_bolsas_concedidas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver).text
#     except:
#         info["numero_bolsas_concedidas"] = "N/A"
#     try:
#         info["numero_discentes_envolvidos"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver).text
#     except:
#         info["numero_discentes_envolvidos"] = "N/A"
#     try:
#         info["faz_parte_de_programa_de_extensao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver).text
#     except:
#         info["faz_parte_de_programa_de_extensao"] = "N/A"
#     try:
#         info["publico_estimado"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver).text
#     except:
#         info["publico_estimado"] = "N/A"
#     try:
#         info["publico_real_atendido"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver).text
#     except:
#         info["publico_real_atendido"] = "N/A"
#     try:
#         info["tipo_de_cadastro"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver).text
#     except:
#         info["tipo_de_cadastro"] = "N/A"
#     try:
#         info["tipo_do_evento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver).text
#     except:
#         info["tipo_do_evento"] = "N/A"
#     try:
#         info["periodo_do_evento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver).text
#     except:
#         info["periodo_do_evento"] = "N/A"
#     try:
#         info["carga_horario"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver).text
#     except:
#         info["carga_horario"] = "N/A"
#     try:
#         info["previsao_n_de_vagas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver).text
#     except:
#         info["previsao_n_de_vagas"] = "N/A"
#     try:
#         info["contato_coordenacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[31]/td", driver).text
#     except:
#         info["contato_email"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver).text
#     try:
#         info["contato_telefone"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver).text
#     except:
#         info["contato_telefone"] = "N/A"

#     return info
