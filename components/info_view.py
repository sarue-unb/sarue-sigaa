import components.selection_components as sc
from config.actions_descryption import *
from tqdm import tqdm

def get_row_data_view(driver, month, year):
    rows_total_data = []
    result_table = sc.get_rows_from_table(driver)
    rows_length = sc.get_rows_len(result_table)
    
    for i in tqdm(range(0, rows_length - 1)): # tqdm is a progress bar
        sc.use_element_by_id(VIEW_FORM_ID_PRE_FIX + str(i) + VIEW_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_view_page(driver)
        sc.add_date_to_item(row_info, month, year)
        rows_total_data.append(row_info)
        
        sc.use_element_by_class("voltar", driver)
        # use_element_by_xpath("/html/body/div[2]/div[2]/form/table/tfoot/tr/td/input", driver)

        result_table = sc.get_rows_from_table(driver)
        
    return rows_total_data

def get_info_from_view_page(driver):
    info = {}

    info["codigo"] = sc.get_info_direct("//html/body/div[2]/div[2]/form/table/tbody/tr[2]/td", driver)
    info["titulo"] = sc.get_info_direct("//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td", driver)

    info["categoria"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td[1]", driver)
    info["abrangencia"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td[2]", driver)
    info["ano"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[1]", driver)
    info["periodo_realizacao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]", driver)

    info["unidade_proponente"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[6]/td", driver)  
    info["unidade_orcamentaria"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[7]/td", driver)
    info["executor_financeiro"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[8]/td", driver)
    info["unidade_coexecutora"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[9]/td", driver)
    info["outras_unidades_envolvidas"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[10]/td", driver)

    info["area_cnpq"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[11]/td[1]", driver)
    info["area_principal"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[11]/td[2]", driver)
    info["qtd_bolsas_solicitadas"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[12]/td[1]", driver)
    info["qtd_bolsas_concedidas"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[12]/td[2]", driver)
    info["tipo_cadastro"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[1]", driver)
    info["convenio_funpec"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]", driver)
    info["publico_alvo_interno"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[14]/td[1]", driver)
    info["publico_alvo_externo"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[14]/td[2]", driver)
    info["publico_estimado_externo"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[15]/td[1]", driver)
    info["publico_estimado_interno"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[15]/td[2]", driver)

    info["publico_real_atingido"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[16]/td", driver)
    
    info["fonte_financiamento"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td[1]", driver)
    info["renovacao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td[2]", driver)

    info["linha_atuacao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[18]/td", driver)
    info["programa_estrategico"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[19]/td", driver)
    info["vinculado_acao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[20]/td", driver)
    info["vinculado_grupo"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[21]/td", driver)
    info["parte_programa_extensao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[22]/td", driver)
    info["tipo_evento"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[24]/td", driver)
    info["periodo_evento"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[25]/td", driver)

    if(info["categoria"] == "EVENTO" or info["categoria"] == "CURSO"):
        info["carga_horaria"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[26]/td[1]", driver)
        info["previsao_vagas"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[26]/td[2]", driver)

    info["situacao"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[27]/td", driver)
    info["reponsavel_acao_nome"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[28]/td", driver)
    info["reponsavel_acao_email"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[29]/td", driver)
    info["reponsavel_acao_telefone"] = sc.get_info_direct("/html/body/div[2]/div[2]/form/table/tbody/tr[30]/td", driver)

    info["estado_realizacao"] = sc.get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[1]")
    info["municipio_realizacao"] = sc.get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[2]", driver)
    info["bairro_realizacao"] = sc.get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[3]", driver)
    info["espaco_realizacao"] = sc.get_info_try_except("/html/body/div[2]/div[2]/form/table/tbody/tr[32]/td/table/tbody/tr[2]/td[4]", driver)

    # Aqui precisa ter paciencia, ate fazer uma função para verificar se a imagem contida é light ou não

    return info