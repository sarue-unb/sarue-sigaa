from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from database_generator.constants import PRINTER_FORM_ID_PRE_FIX, PRINTER_FORM_ID_POS_FIX
import time

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
    # This is being done directly through XPATH
    # But we could also do it by using the table Id
    rows = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/form[2]/table/tbody/tr')
    return len(rows)

def get_rows_len(result_table):
     return len(result_table.find_elements(By.XPATH, ".//tr"))

def get_rows_from_table(driver):
        return driver.find_element(By.ID, "listagem")

def get_row_data( driver):
    rows_total_data = []
    result_table= get_rows_from_table(driver)
    rows_length = get_rows_len(result_table)
    print("Rows length:", rows_length)
    
    for i in range(0, rows_length - 1):
            use_element_by_id(PRINTER_FORM_ID_PRE_FIX + str(i) + PRINTER_FORM_ID_POS_FIX, result_table)
            
            row_info = get_info_from_print_page(driver)
            rows_total_data.append(row_info)
            
            use_element_by_class("voltar", driver)
            
            result_table = get_rows_from_table(driver)
            
    return rows_total_data

def get_info_from_print_page(driver):
    try:
        # to-do: add map here with try except for each field
        
        info = {}
        info["codigo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td", driver).text
        info["titulo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td", driver).text
        info["ano"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver).text
        info["periodo_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td", driver).text
        info["tipo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td", driver).text
        info["situacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td", driver).text
        info["munincipio_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver).text
        info["espaco_de_realizacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver).text
        info["abrangencia"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver).text
        info["publico_alvo"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver).text
        info["unidade_proponente"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver).text
        info["unidade_orcamentaria"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver).text
        #This is a table, contrary to the other fields
        # info["outras_unidades_envolvidas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td/table/tbody/tr/td", driver).text
        info["area_principal"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver).text
        info["area_do_cnpq"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver).text
        info["fonte_de_financiamento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver).text
        info["convenio_funpec"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver).text
        info["renovacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver).text
        info["numero_bolsas_solicitadas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver).text
        info["numero_bolsas_concedidas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver).text
        info["numero_discentes_envolvidos"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver).text
        info["faz_parte_de_programa_de_extensao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver).text
        info["publico_estimado"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver).text
        info["publico_real_atendido"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver).text
        info["tipo_de_cadastro"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver).text
        info["tipo_do_evento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver).text
        info["periodo_do_evento"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver).text
        info["carga_horario"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver).text
        info["previsao_n_de_vagas"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver).text
        info["contato_coordenacao"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[31]/td", driver).text
        info["contato_email"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver).text
        info["contato_telefone"] = get_element_by_xpath("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver).text
    except:
        return info
    return info
