#info_printer.py
##@file 
#@brief Contém funções para extrair informações de uma página de impressão.

#Este módulo fornece funções para extrair várias informações de uma página de impressão.
import components.selection_components as sc
from config.output_format import clear_strings
from config.display_descryption import SIZE_TERMINAL
from config.xapths.actions_xpath_descryption import *
from config.ids.actions_id_descryption import *
from tqdm import tqdm

def get_row_data_printer(driver, month:int, year:int, cnpq=None):
    """
    Obtém dados da linha de uma impressora.

    Esta função recupera dados da linha de uma página de impressora e retorna uma lista de informações.

    @param driver: Objeto WebDriver para interagir com a página da web.
    @param month: O mês para o qual os dados estão sendo recuperados.
    @param year: O ano para o qual os dados estão sendo recuperados.
    @param cnpq: Informações CNPQ (opcional).

    @return: Uma lista de dados da linha.
    """
    rows_total_data = []
    result_table = sc.get_rows_from_table(driver)
    rows_length = sc.get_rows_len(result_table)

    if cnpq != None:
        desc = f'{month:02d}/{year} - {cnpq}'
    else:
        desc = f'{month:02d}/{year}'
    for i in tqdm(range(0, rows_length - 1), desc=desc, bar_format='{desc} - {elapsed} {bar} {n_fmt}/{total_fmt} - {percentage:.0f}%', ncols=SIZE_TERMINAL): # tqdm is a progress bar
        sc.use_element_by_id(PRINTER_FORM_ID_PRE_FIX + str(i) + PRINTER_FORM_ID_POS_FIX, result_table)
        
        row_info = get_info_from_print_page(driver)
        sc.add_date_to_item(row_info, month, year)
        rows_total_data.append(row_info)
        
        sc.use_element_by_class("voltar", driver)

        result_table = sc.get_rows_from_table(driver)
        
    return rows_total_data

def get_info_from_print_page(driver):
    """
    Obtém informações de uma página de impressão.

    Esta função extrai informações de uma página de impressão e retorna um dicionário.

    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Um dicionário contendo informações da página de impressão.
    """
    info = {}

    ## Padrao a todas
    info["codigo"] = sc.get_info(XPATHS_CODIGO, driver)
    info["titulo"] = sc.get_info(XPATHS_TITULO, driver)
    info["ano"] = sc.get_info(XPATHS_ANO, driver)
    info["periodo_de_realizacao"] = sc.get_info(XPATHS_PERIODO_DE_REALIZACAO, driver)
    info["tipo"] = sc.get_info(XPATHS_TIPO, driver)
    info["situacao"] = sc.get_info(XPATHS_SITUACAO, driver)
    ##
    
    ## FIX: Acoes canceladas
    if 'xxx' in info["codigo"]:
        info["codigo"] = info["codigo"] + " _ " + info["titulo"]
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

    if sc.get_element_by_xpath(XPATHS_OTHER_TABLES, driver):
        qtd_tabelas = sc.get_qtd_tables_by_xpath(XPATHS_OTHER_TABLES, driver)

        if (qtd_tabelas >= 2):
            info = get_info_objetivos(info, XPATHS_OBJETIVOS, driver)
            if (sc.get_qtd_tables_by_xpath(XPATHS_OTHER_TABLES, driver) >= 3):
                info = get_info_team_members(info, ID_TEAM_MEMBERS, driver)
            
    return info

def get_info_from_printer_type_curso(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'CURSO'.

    Esta função extrai informações específicas do tipo 'CURSO' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'CURSO'.
    """
    info["munincipio_de_realizacao"] = sc.get_info(CURSO_XPATHS_MUNICIPIO_DE_REALIZACAO, driver)
    info["espaco_de_realizacao"] = sc.get_info(CURSO_XPATHS_ESPACO_DE_REALIZACAO, driver)
    info["abrangencia"] = sc.get_info(CURSO_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(CURSO_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(CURSO_XPATHS_CURSO_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(CURSO_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(CURSO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(CURSO_XPATHS_AREA_PRINCIPAL, driver)
    info["area_do_cnpq"] = sc.get_info(CURSO_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(CURSO_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(CURSO_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(CURSO_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(CURSO_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(CURSO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    info["numero_discentes_envolvidos"] = sc.get_info(CURSO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info(CURSO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO, driver)
    info["publico_estimado"] = sc.get_info(CURSO_XPATHS_PUBLICO_ESTIMADO, driver)
    info["publico_real_atendido"] = sc.get_info(CURSO_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
    info["cadastro_tipo"] = sc.get_info(CURSO_XPATHS_CADASTRO_TIPO, driver)
    info["cadastro_categoria"] = sc.get_info(CURSO_XPATHS_CADASTRO_CATEGORIA, driver)
    info["cadastro_subcategoria"] = sc.get_info(CURSO_XPATHS_CADASTRO_SUBCATEGORIA, driver)
    info["periodo_de_execucao"] = sc.get_info(CURSO_XPATHS_PERIODO_DE_EXECUCAO, driver)
    info["carga_horaria"] = sc.get_info(CURSO_XPATHS_CARGA_HORARIO, driver)
    info["previsao_n_de_vagas"] = sc.get_info(CURSO_XPATHS_PREVISAO_N_DE_VAGAS, driver)
    info["contato_coordenacao"] = sc.get_info(CURSO_XPATHS_CONTATO_COORDENACAO, driver)
    info["contato_email"] = sc.get_info(CURSO_XPATHS_CONTATO_EMAIL, driver)
    info["contato_telefone"] = sc.get_info(CURSO_XPATHS_CONTATO_TELEFONE, driver)

    return info

def get_info_from_printer_type_evento(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'EVENTO'.

    Esta função extrai informações específicas do tipo 'EVENTO' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'EVENTO'.
    """
    info["munincipio_de_realizacao"] = sc.get_info(EVENTO_XPATHS_MUNINCIPIO_DE_REALIZACAO, driver)
    info["espaco_de_realizacao"] = sc.get_info(EVENTO_XPATHS_ESPACO_DE_REALIZACAO, driver)
    info["abrangencia"] = sc.get_info(EVENTO_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(EVENTO_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(EVENTO_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(EVENTO_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(EVENTO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(EVENTO_XPATHS_AREA_PRINCIPAL, driver)
    info["area_do_cnpq"] = sc.get_info(EVENTO_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(EVENTO_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(EVENTO_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(EVENTO_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(EVENTO_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(EVENTO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    info["numero_discentes_envolvidos"] = sc.get_info(EVENTO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
    info["faz_parte_de_programa_de_extensao"] = sc.get_info(EVENTO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO, driver)
    info["publico_estimado"] = sc.get_info(EVENTO_XPATHS_PUBLICO_ESTIMADO, driver)   
    info["publico_real_atendido"] = sc.get_info(EVENTO_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
    info["cadastro_tipo"] = sc.get_info(EVENTO_XPATHS_CADASTRO_TIPO, driver)
    info["cadastro_categoria"] = sc.get_info(EVENTO_XPATHS_CADASTRO_CATEGORIA, driver) 
    info["periodo_de_execucao"] = sc.get_info(EVENTO_XPATHS_PERIODO_DE_EXECUCAO, driver)
    info["carga_horario"] = sc.get_info(EVENTO_XPATHS_CARGA_HORARIO, driver)
    info["previsao_n_de_vagas"] = sc.get_info(EVENTO_XPATHS_PREVISAO_N_DE_VAGAS, driver)
    
    info["contato_coordenacao"] = sc.get_info(EVENTO_XPATHS_CONTATO_COORDENACAO, driver)
    info["contato_email"] = sc.get_info(EVENTO_XPATHS_CONTATO_EMAIL, driver)
    info["contato_telefone"] = sc.get_info(EVENTO_XPATHS_CONTATO_TELEFONE, driver)
    
    return info

def get_info_from_printer_type_prestacao_servico(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'PRESTAÇÃO DE SERVIÇO'.

    Esta função extrai informações específicas do tipo 'PRESTAÇÃO DE SERVIÇO' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'PRESTAÇÃO DE SERVIÇO'.
    """
    # Nenhuma cadastrada no sigaa
    # BASEADO EM UM E-MAIL. SE EXISTIR UM EXEMPLO DENTRO DO SIGAA. FAVOR ATUALIZAR
    info["abrangencia"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_AREA_PRINCIPAL, driver)    
    info["area_do_cnpq"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    info["numero_discentes_envolvidos"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
    info["publico_estimado"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_PUBLICO_ESTIMADO, driver)
    info["publico_real_atendido"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
    info["cadastro_tipo"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CADASTRO_TIPO, driver)
    info["cadastro_categoria"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CADASTRO_CATEGORIA, driver)
    
    info["contato_coordenacao"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CONTATO_COORDENACAO, driver)
    info["contato_email"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CONTATO_EMAIL, driver)
    info["contato_telefone"] = sc.get_info(PRESTACAO_SERVICO_XPATHS_CONTATO_TELEFONE, driver)

    return info

def get_info_from_printer_type_produto(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'PRODUTO'.

    Esta função extrai informações específicas do tipo 'PRODUTO' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'PRODUTO'.
    """
    info["abrangencia"] = sc.get_info(PRODUTO_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(PRODUTO_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(PRODUTO_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(PRODUTO_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(PRODUTO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(PRODUTO_XPATHS_AREA_PRINCIPAL, driver)
    info["area_do_cnpq"] = sc.get_info(PRODUTO_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(PRODUTO_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(PRODUTO_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(PRODUTO_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(PRODUTO_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(PRODUTO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    info["numero_discentes_envolvidos"] = sc.get_info(PRODUTO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
    info["publico_estimado"] = sc.get_info(PRODUTO_XPATHS_PUBLICO_ESTIMADO, driver)
    info["publico_real_atendido"] = sc.get_info(PRODUTO_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
    info["cadastro_tipo"] = sc.get_info(PRODUTO_XPATHS_CADASTRO_TIPO, driver)
    info["cadastro_categoria"] = sc.get_info(PRODUTO_XPATHS_CADASTRO_CATEGORIA, driver)
    info["triagem"] = sc.get_info(PRODUTO_XPATHS_TRIAGEM, driver)

    info["contato_coordenacao"] = sc.get_info(PRODUTO_XPATHS_CONTATO_COORDENACAO, driver)
    info["contato_email"] = sc.get_info(PRODUTO_XPATHS_CONTATO_EMAIL, driver)
    info["contato_telefone"] = sc.get_info(PRODUTO_XPATHS_CONTATO_TELEFONE, driver)
    
    return info

def get_info_from_printer_type_programa(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'PROGRAMA'.

    Esta função extrai informações específicas do tipo 'PROGRAMA' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'PROGRAMA'.
    """
    info["abrangencia"] = sc.get_info(PROGRAMA_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(PROGRAMA_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(PROGRAMA_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(PROGRAMA_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(PROGRAMA_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(PROGRAMA_XPATHS_AREA_PRINCIPAL, driver)
    info["area_do_cnpq"] = sc.get_info(PROGRAMA_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(PROGRAMA_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(PROGRAMA_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(PROGRAMA_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(PROGRAMA_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(PROGRAMA_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    info["numero_discentes_envolvidos"] = sc.get_info(PROGRAMA_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
    info["publico_estimado"] = sc.get_info(PROGRAMA_XPATHS_PUBLICO_ESTIMADO, driver)
    info["publico_real_atendido"] = sc.get_info(PROGRAMA_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
    info["cadastro_tipo"] = sc.get_info(PROGRAMA_XPATHS_CADASTRO_TIPO, driver)

    info["contato_coordenacao"] = sc.get_info(PROGRAMA_XPATHS_CONTATO_COORDENACAO, driver)
    info["contato_email"] = sc.get_info(PROGRAMA_XPATHS_CONTATO_EMAIL, driver)
    info["contato_telefone"] = sc.get_info(PROGRAMA_XPATHS_CONTATO_TELEFONE, driver)

    return info

def get_info_from_printer_type_projeto(info:dict, driver):
    """
    Obtém informações de uma impressora do tipo 'PROJETO'.

    Esta função extrai informações específicas do tipo 'PROJETO' de uma página de impressora.

    @param info: Dicionário para armazenar informações extraídas.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações específicas de 'PROJETO'.
    """
    info["munincipio_de_realizacao"] = sc.get_info(PROJETO_XPATHS_MUNINCIPIO_DE_REALIZACAO, driver)
    info["espaco_de_realizacao"] = sc.get_info(PROJETO_XPATHS_ESPACO_DE_REALIZACAO, driver)
    info["abrangencia"] = sc.get_info(PROJETO_XPATHS_ABRANGENCIA, driver)
    info["publico_alvo"] = sc.get_info(PROJETO_XPATHS_PUBLICO_ALVO, driver)
    info["unidade_proponente"] = sc.get_info(PROJETO_XPATHS_UNIDADE_PROPONENTE, driver)
    info["unidade_orcamentaria"] = sc.get_info(PROJETO_XPATHS_UNIDADE_ORCAMENTARIA, driver)
    info["outras_unidades_envolvidas"] = sc.get_info(PROJETO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS, driver)
    info["area_principal"] = sc.get_info(PROJETO_XPATHS_AREA_PRINCIPAL, driver)
    info["area_do_cnpq"] = sc.get_info(PROJETO_XPATHS_AREA_DO_CNPQ, driver)
    info["fonte_de_financiamento"] = sc.get_info(PROJETO_XPATHS_FONTE_DE_FINANCIAMENTO, driver)
    info["convenio_funpec"] = sc.get_info(PROJETO_XPATHS_CONVENIO_FUNPEC, driver)
    info["renovacao"] = sc.get_info(PROJETO_XPATHS_RENOVACAO, driver)
    info["numero_bolsas_solicitadas"] = sc.get_info(PROJETO_XPATHS_NUMERO_BOLSAS_SOLICITADAS, driver)
    info["numero_bolsas_concedidas"] = sc.get_info(PROJETO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS, driver)
    
    if(sc.get_qtd_tables_by_xpath_relatorio(XPATHS_RELATORIO, driver) == 35 and info["codigo"] != "PJ314-2022"):
        info["numero_discentes_envolvidos"] = sc.get_info(PROJETO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS_ALTERNATIVE, driver)
        info["faz_parte_de_programa_de_extensao"] = sc.get_info(PROJETO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO_ALTERNATIVE, driver)
        info["grupo_permanente"] = sc.get_info(PROJETO_XPATHS_GRUPO_PERMANENTE_ALTERNATIVE, driver)
        info["publico_estimado"] = sc.get_info(PROJETO_XPATHS_PUBLICO_ESTIMADO_ALTERNATIVE, driver)
        info["publico_real_atendido"] = sc.get_info(PROJETO_XPATHS_PUBLICO_REAL_ATENDIDO_ALTERNATIVE, driver)
        info["cadastro_tipo"] = sc.get_info(PROJETO_XPATHS_CADASTRO_TIPO_ALTERNATIVE, driver)
        
        info["contato_coordenacao"] = sc.get_info(PROJETO_XPATHS_CONTATO_COORDENACAO_ALTERNATIVE, driver)
        info["contato_email"] = sc.get_info(PROJETO_XPATHS_CONTATO_EMAIL_ALTERNATIVE, driver)
        info["contato_telefone"] = sc.get_info(PROJETO_XPATHS_CONTATO_TELEFONE_ALTERNATIVE, driver)
    else:
        info["numero_discentes_envolvidos"] = sc.get_info(PROJETO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS, driver)
        info["faz_parte_de_programa_de_extensao"] = sc.get_info(PROJETO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO, driver)
        info["grupo_permanente"] = sc.get_info(PROJETO_XPATHS_GRUPO_PERMANENTE, driver)
        info["publico_estimado"] = sc.get_info(PROJETO_XPATHS_PUBLICO_ESTIMADO, driver)
        info["publico_real_atendido"] = sc.get_info(PROJETO_XPATHS_PUBLICO_REAL_ATENDIDO, driver)
        info["cadastro_tipo"] = sc.get_info(PROJETO_XPATHS_CADASTRO_TIPO, driver)
        
        info["contato_coordenacao"] = sc.get_info(PROJETO_XPATHS_CONTATO_COORDENACAO, driver)
        info["contato_email"] = sc.get_info(PROJETO_XPATHS_CONTATO_EMAIL, driver)
        info["contato_telefone"] = sc.get_info(PROJETO_XPATHS_CONTATO_TELEFONE, driver)

    return info

def get_info_objetivos(info: dict, xpath: str, driver):
    """
    Obtém informações sobre objetivos a partir de um XPath específico.

    Esta função extrai informações sobre objetivos de um XPath especificado na página da web.

    @param info: Dicionário para armazenar informações extraídas.
    @param xpath: XPath para localizar o elemento contendo informações de objetivo.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações de objetivo.
    """
    tipo = sc.get_element_by_xpath(xpath, driver)
    
    if tipo != None:
        qtd = sc.get_rows_len(tipo)
        info["objetivos"] = [int(sc.get_info(XPATHS_OBJETIVOS_PRE_FIX + str(i) + XPATHS_OBJETIVOS_POS_FIX, driver)) for i in range(1, qtd)]
        
    return info

def get_info_team_members(info: dict, id: str, driver):
    """
    Obtém informações sobre membros da equipe a partir de um ID específico.

    Esta função extrai informações sobre membros da equipe de um ID específico na página da web.

    @param info: Dicionário para armazenar informações extraídas.
    @param id: ID para localizar o elemento contendo informações de membros da equipe.
    @param driver: Objeto WebDriver para interagir com a página da web.

    @return: Dicionário atualizado com informações de membros da equipe.
    """
    tipo = sc.get_element_by_id(id, driver)

    if tipo != None:
        qtd = sc.get_rows_len(tipo)
        membros = []
        
        for i in range(1, qtd):
            m_equipe_nome = sc.get_info(ID_TEAM_MEMBERS_PRE_FIX + str(i) + ID_TEAM_MEMBERS_POS_FIX_NAME, driver).upper()
            m_equipe_nome = clear_strings(m_equipe_nome)
            
            m_equipe_categoria = sc.get_info(ID_TEAM_MEMBERS_PRE_FIX + str(i) + ID_TEAM_MEMBERS_POS_FIX_CATEGORY, driver).capitalize()
            m_equipe_funcao = sc.get_info(ID_TEAM_MEMBERS_PRE_FIX + str(i) + ID_TEAM_MEMBERS_POS_FIX_FUNCTION, driver).capitalize()
            m_equipe_departamento = sc.get_info(ID_TEAM_MEMBERS_PRE_FIX + str(i) + ID_TEAM_MEMBERS_POS_FIX_DEPARTAMENT, driver).capitalize()
            m_equipe_situacao = sc.get_info(ID_TEAM_MEMBERS_PRE_FIX + str(i) + ID_TEAM_MEMBERS_POS_FIX_STATUS, driver).capitalize()
            
            membros.append([m_equipe_nome, m_equipe_categoria, m_equipe_funcao, m_equipe_departamento, m_equipe_situacao])
           
        info["membros_da_equipe"] = membros
    return info
