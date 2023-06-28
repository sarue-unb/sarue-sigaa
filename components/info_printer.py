from selenium.webdriver.common.by import By
from database_generator.constants import OBJECT_FORM_ID

def get_qtd_tables_by_xpath(xpath: str, driver):
    form = driver.find_element(By.XPATH, xpath)

    return len(form.find_elements(By.XPATH, "table"))

def get_element_by_xpath(value: int, driver):
    return driver.find_element(By.XPATH, value)

def get_element_by_id(id: str, driver):
    return driver.find_element(By.ID, id)
    
def get_element_by_class(class_name: str, driver):
    return driver.find_element(By.CLASS_NAME, class_name)

def get_rows_len(result_table):
     return len(result_table.find_elements(By.XPATH, ".//tr"))

def get_info_try_except(xpath, driver):
    try:
        return get_element_by_xpath(xpath, driver).text
    except:
        return "N/A"
    
def get_info_direct(xpath, driver):
    return get_element_by_xpath(xpath, driver).text

def get_info_from_print_page(driver):
    info = {}

    ## Padrao a todas
    info["codigo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td", driver)
    info["titulo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td", driver)
    info["ano"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver)
    info["periodo_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td", driver)
    info["tipo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td", driver)
    info["situacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td", driver)
    ##
    
    if(info["tipo"] == "CURSO"):
        info = get_info_from_printer_type_curso(info, driver)

    elif(info["tipo"] == "EVENTO"):
        info = get_info_from_printer_type_evento(info, driver)

    elif info["tipo"] == "PRESTAÇÃO DE SERVIÇO":
        info = get_info_from_printer_type_prestacao_servico(info, driver)

    elif info["tipo"] == "PRODUTO":
        info = get_info_from_printer_type_produto(info, driver)

    elif info["tipo"] == "PROGRAMA":
        info = get_info_from_printer_type_programa(info, driver)

    elif info["tipo"] == "PROJETO":
        info = get_info_from_printer_type_projeto(info, driver)

    if (get_qtd_tables_by_xpath("/html/body/div/div[2]/form", driver) > 1):
        info = get_info_objetivos(info, "/html/body/div/div[2]/form/table[2]", driver)
    
    return info

def get_info_from_printer_type_curso(info:dict, driver):
    info["munincipio_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["publico_estimado"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_real_atendido"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["tipo_de_cadastro"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["modalidade_do_curso"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["tipo_do_curso"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["periodo_do_curso"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["carga_horario"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)
    info["previsao_n_de_vagas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td", driver)

    info["contato_coordenacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver)
    info["contato_email"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver)
    info["contato_telefone"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td", driver)
   
    return info

def get_info_from_printer_type_evento(info:dict, driver):
    info["munincipio_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["publico_estimado"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_real_atendido"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["tipo_de_cadastro"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["tipo_do_evento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["periodo_do_evento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["carga_horario"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["previsao_n_de_vagas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)

    info["contato_coordenacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver)
    info["contato_email"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver)
    info["contato_telefone"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td", driver)
     
    return info

def get_info_from_printer_type_prestacao_servico(info:dict, driver):
    # Nenhuma cadastrada no sigaa
    return info

def get_info_from_printer_type_produto(info:dict, driver):
    info["abrangencia"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["publico_alvo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["unidade_proponente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["unidade_orcamentaria"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["area_principal"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["area_do_cnpq"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["fonte_de_financiamento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["convenio_funpec"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)   
    info["renovacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["publico_estimado"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)  
    info["publico_real_atendido"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["tipo_de_cadastro"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)
    info["tipo_produto"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["triagem"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)

    info["contato_coordenacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["contato_email"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["contato_telefone"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)

    return info

def get_info_from_printer_type_programa(info:dict, driver):
    info["abrangencia"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["publico_alvo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["unidade_proponente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["unidade_orcamentaria"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["area_principal"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["area_do_cnpq"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["fonte_de_financiamento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["convenio_funpec"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)   
    info["renovacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver)
    info["publico_estimado"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)  
    info["publico_real_atendido"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["tipo_de_cadastro"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    
    info["contato_coordenacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["contato_email"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["contato_telefone"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)

    return info

def get_info_from_printer_type_projeto(info:dict, driver):
    info["munincipio_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["grupo_permanente"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_estimado"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)  
    info["publico_real_atendido"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["tipo_de_cadastro"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    
    info["contato_coordenacao"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["contato_email"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)
    info["contato_telefone"] = get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td", driver)

    return info

def get_info_objetivos(info: dict, xpath: str, driver):
    tipo = get_element_by_xpath(xpath, driver)
    
    if tipo != None:
        qtd = get_rows_len(tipo)
        info["objetivos"] = [int(get_info_direct("//html/body/div/div[2]/form/table[2]/tbody/tr[{}]/td[1]".format(i), driver)) for i in range(1, qtd)]
        
    return info