import components.selection_components as sc
from database_generator.constants import *
from output_format import SIZE_TERMINAL
from tqdm import tqdm

def get_row_data_printer(driver, month, year):
    rows_total_data = []
    result_table = sc.get_rows_from_table(driver)
    rows_length = sc.get_rows_len(result_table)

    desc = f'{month:02d}/{year}'
    for i in tqdm(range(0, rows_length - 1), desc=desc, bar_format='{desc} - {elapsed} {bar} {n_fmt}/{total_fmt} - {percentage:.0f}%', ncols=SIZE_TERMINAL): # tqdm is a progress bar
        sc.use_element_by_id(PRINTER_FORM_ID_PRE_FIX + str(i) + PRINTER_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_print_page(driver)
        sc.add_date_to_item(row_info, month, year)
        rows_total_data.append(row_info)
        
        sc.use_element_by_class("voltar", driver)
        # use_element_by_xpath("/html/body/div/div[4]/p/table/tbody/tr/td[1]", driver) # Does not work, voltar element can also be found in the table /html/body/div/div[2]/p/table/tbody/tr/td[1]

        result_table = sc.get_rows_from_table(driver)
        
    return rows_total_data

def get_info_from_print_page(driver):
    info = {}

    ## Padrao a todas
    info["codigo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td", driver)
    info["titulo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td", driver)
    info["ano"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver)
    info["periodo_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td", driver)
    info["tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td", driver)
    info["situacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td", driver)
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

    if (sc.get_qtd_tables_by_xpath("/html/body/div/div[2]/form", driver) > 1):
        info = get_info_objetivos(info, "/html/body/div/div[2]/form/table[2]", driver)
    
    return info

def get_info_from_printer_type_curso(info:dict, driver):
    info["munincipio_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["cadastro_categoria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["cadastro_subcategoria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["periodo_de_execucao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["carga_horario"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)
    info["previsao_n_de_vagas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td", driver)

    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td", driver)
   
    return info

def get_info_from_printer_type_evento(info:dict, driver):
    info["munincipio_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["cadastro_categoria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["periodo_de_execucao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["carga_horario"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["previsao_n_de_vagas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)

    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td", driver)
     
    return info

def get_info_from_printer_type_prestacao_servico(info:dict, driver):
    # Nenhuma cadastrada no sigaa
    # BASEADO EM UM E-MAIL. SE EXISTIR UM EXEMPLO DENTRO DO SIGAA. FAVOR ATUALIZAR
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver)
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["cadastro_categoria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)
    
    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)

    return info

def get_info_from_printer_type_produto(info:dict, driver):
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)
    info["cadastro_categoria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["triagem"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)

    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)

    return info

def get_info_from_printer_type_programa(info:dict, driver):
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver)
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    
    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)

    return info

def get_info_from_printer_type_projeto(info:dict, driver):
    info["munincipio_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td", driver)
    info["espaco_de_realizacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td", driver)
    info["abrangencia"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td", driver)
    info["publico_alvo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td", driver)
    info["unidade_proponente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td", driver)
    info["unidade_orcamentaria"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td", driver)
    info["area_principal"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td", driver)
    info["area_do_cnpq"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td", driver)
    info["fonte_de_financiamento"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td", driver)
    info["convenio_funpec"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td", driver)   
    info["renovacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td", driver)
    info["numero_bolsas_solicitadas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td", driver) 
    info["numero_bolsas_concedidas"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td", driver)
    info["numero_discentes_envolvidos"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td", driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td", driver)
    info["grupo_permanente"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td", driver)  
    info["publico_estimado"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td", driver)  
    info["publico_real_atendido"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td", driver)
    info["cadastro_tipo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td", driver)
    
    info["contato_coordenacao"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td", driver)
    info["contato_email"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td", driver)
    info["contato_telefone"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td", driver)

    return info

def get_info_objetivos(info: dict, xpath: str, driver):
    tipo = sc.get_element_by_xpath(xpath, driver)
    
    if tipo != None:
        qtd = sc.get_rows_len(tipo)
        info["objetivos"] = [int(sc.get_info_direct("//html/body/div/div[2]/form/table[2]/tbody/tr[{}]/td[1]".format(i), driver)) for i in range(1, qtd)]
        
    return info