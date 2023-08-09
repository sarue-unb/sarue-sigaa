# Existe um XPATH em get_info_objetivos() em components/info_printer.py
XPATHS_OBJETIVOS_PRE_FIX = '//html/body/div/div[2]/form/table[2]/tbody/tr['
XPATHS_OBJETIVOS_POS_FIX = ']/td[1]'

ID_TEAM_MEMBERS_PRE_FIX = "//*[contains(@id, 'j_id_jsp_')]//*[contains(@id, ':tbEquipe:tbody_element')]/tr["
XPATHS_TEAM_MEMBERS_POS_FIX_NAME = ']/td[1]'
XPATHS_TEAM_MEMBERS_POS_FIX_CATEGORY = ']/td[2]'
XPATHS_TEAM_MEMBERS_POS_FIX_FUNCTION = ']/td[3]'
XPATHS_TEAM_MEMBERS_POS_FIX_DEPARTAMENT = ']/td[4]'
XPATHS_TEAM_MEMBERS_POS_FIX_STATUS = ']/td[5]'

PRINTER_FORM_ID_PRE_FIX = 'form:j_id_jsp_1439633680_522:'
PRINTER_FORM_ID_POS_FIX = ':imprimir'

VIEW_FORM_ID_PRE_FIX = 'form:j_id_jsp_1439633680_522:'
VIEW_FORM_ID_POS_FIX = ':visualizar'

OBJECT_FORM_ID = 'j_id_jsp_345370874_1:tbOds:tbody_element'

# PADRAO A TODAS
XPATHS_CODIGO = '//html/body/div/div[2]/form/table[1]/tbody/tr[1]/td'
XPATHS_TITULO = '//html/body/div/div[2]/form/table[1]/tbody/tr[2]/td'
XPATHS_ANO = '//html/body/div/div[2]/form/table[1]/tbody/tr[3]/td'
XPATHS_PERIODO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[4]/td'
XPATHS_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[5]/td'
XPATHS_SITUACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[6]/td'
    
XPATHS_OTHER_TABLES = '/html/body/div/div[2]/form'
XPATHS_OBJETIVOS = '/html/body/div/div[2]/form/table[2]'
ID_TEAM_MEMBERS = 'j_id_jsp_345370874_1:tbEquipe'

# CURSO
CURSO_XPATHS_MUNICIPIO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
CURSO_XPATHS_ESPACO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
CURSO_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
CURSO_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
CURSO_XPATHS_CURSO_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
CURSO_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
CURSO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
CURSO_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
CURSO_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'
CURSO_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
CURSO_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td'   
CURSO_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
CURSO_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td' 
CURSO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'
CURSO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'
CURSO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'
CURSO_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td'  
CURSO_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td'
CURSO_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'
CURSO_XPATHS_CADASTRO_CATEGORIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td'
CURSO_XPATHS_CADASTRO_SUBCATEGORIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td'
CURSO_XPATHS_PERIODO_DE_EXECUCAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td'
CURSO_XPATHS_CARGA_HORARIO = '//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td'
CURSO_XPATHS_PREVISAO_N_DE_VAGAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td'

CURSO_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td'
CURSO_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td'
CURSO_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td'

# EVENTO
EVENTO_XPATHS_MUNINCIPIO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
EVENTO_XPATHS_ESPACO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
EVENTO_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
EVENTO_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
EVENTO_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
EVENTO_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
EVENTO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
EVENTO_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
EVENTO_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'
EVENTO_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
EVENTO_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td'   
EVENTO_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
EVENTO_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td' 
EVENTO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'
EVENTO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'
EVENTO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'
EVENTO_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td'  
EVENTO_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td'
EVENTO_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'
EVENTO_XPATHS_CADASTRO_CATEGORIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td'
EVENTO_XPATHS_PERIODO_DE_EXECUCAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td'
EVENTO_XPATHS_CARGA_HORARIO = '//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td'
EVENTO_XPATHS_PREVISAO_N_DE_VAGAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td'

EVENTO_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[32]/td'
EVENTO_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[33]/td'
EVENTO_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[34]/td'
    
# PRESTACAO_SERVICO
# Nenhuma cadastr[ada no sigaa
# BASEADO EM UM E-MAIL. SE EXISTIR UM EXEMPLO DENtr[O DO SIGAA. FAVOR ATUALIZAR
PRESTACAO_SERVICO_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
PRESTACAO_SERVICO_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
PRESTACAO_SERVICO_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
PRESTACAO_SERVICO_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
PRESTACAO_SERVICO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
PRESTACAO_SERVICO_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
PRESTACAO_SERVICO_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
PRESTACAO_SERVICO_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
PRESTACAO_SERVICO_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'   
PRESTACAO_SERVICO_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
PRESTACAO_SERVICO_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td' 
PRESTACAO_SERVICO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
PRESTACAO_SERVICO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td'
PRESTACAO_SERVICO_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'  
PRESTACAO_SERVICO_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'
PRESTACAO_SERVICO_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'
PRESTACAO_SERVICO_XPATHS_CADASTRO_CATEGORIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td'

PRESTACAO_SERVICO_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'
PRESTACAO_SERVICO_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td'
PRESTACAO_SERVICO_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td'

# PRODUTO
PRODUTO_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
PRODUTO_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
PRODUTO_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
PRODUTO_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
PRODUTO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
PRODUTO_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
PRODUTO_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
PRODUTO_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
PRODUTO_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'   
PRODUTO_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
PRODUTO_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td' 
PRODUTO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
PRODUTO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td'
PRODUTO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'
PRODUTO_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'  
PRODUTO_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'
PRODUTO_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td'
PRODUTO_XPATHS_CADASTRO_CATEGORIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td'
PRODUTO_XPATHS_TRIAGEM = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'

PRODUTO_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[27]/td'
PRODUTO_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td'
PRODUTO_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td'

#PROGRAMA
PROGRAMA_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
PROGRAMA_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
PROGRAMA_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
PROGRAMA_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
PROGRAMA_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
PROGRAMA_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
PROGRAMA_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
PROGRAMA_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
PROGRAMA_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'   
PROGRAMA_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
PROGRAMA_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td' 
PROGRAMA_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
PROGRAMA_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td'
PROGRAMA_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'  
PROGRAMA_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'
PROGRAMA_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'

PROGRAMA_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td'
PROGRAMA_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'
PROGRAMA_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td'

# PROJETO
PROJETO_XPATHS_MUNINCIPIO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[7]/td'
PROJETO_XPATHS_ESPACO_DE_REALIZACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[8]/td'
PROJETO_XPATHS_ABRANGENCIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[9]/td'
PROJETO_XPATHS_PUBLICO_ALVO = '//html/body/div/div[2]/form/table[1]/tbody/tr[10]/td'
PROJETO_XPATHS_UNIDADE_PROPONENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[11]/td'
PROJETO_XPATHS_UNIDADE_ORCAMENTARIA = '//html/body/div/div[2]/form/table[1]/tbody/tr[12]/td'
PROJETO_XPATHS_OUTRAS_UNIDADES_ENVOLVIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[13]/td'
PROJETO_XPATHS_AREA_PRINCIPAL = '//html/body/div/div[2]/form/table[1]/tbody/tr[14]/td'
PROJETO_XPATHS_AREA_DO_CNPQ = '//html/body/div/div[2]/form/table[1]/tbody/tr[15]/td'
PROJETO_XPATHS_FONTE_DE_FINANCIAMENTO = '//html/body/div/div[2]/form/table[1]/tbody/tr[16]/td'
PROJETO_XPATHS_CONVENIO_FUNPEC = '//html/body/div/div[2]/form/table[1]/tbody/tr[17]/td'   
PROJETO_XPATHS_RENOVACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[18]/td'
PROJETO_XPATHS_NUMERO_BOLSAS_SOLICITADAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[19]/td' 
PROJETO_XPATHS_NUMERO_BOLSAS_CONCEDIDAS = '//html/body/div/div[2]/form/table[1]/tbody/tr[20]/td'
PROJETO_XPATHS_NUMERO_DISCENTES_ENVOLVIDOS = '//html/body/div/div[2]/form/table[1]/tbody/tr[21]/td'
PROJETO_XPATHS_FAZ_PARTE_DE_PROGRAMA_DE_EXTENSAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[22]/td'
PROJETO_XPATHS_GRUPO_PERMANENTE = '//html/body/div/div[2]/form/table[1]/tbody/tr[23]/td'  
PROJETO_XPATHS_PUBLICO_ESTIMADO = '//html/body/div/div[2]/form/table[1]/tbody/tr[24]/td'  
PROJETO_XPATHS_PUBLICO_REAL_ATENDIDO = '//html/body/div/div[2]/form/table[1]/tbody/tr[25]/td'
PROJETO_XPATHS_CADASTRO_TIPO = '//html/body/div/div[2]/form/table[1]/tbody/tr[26]/td'

PROJETO_XPATHS_CONTATO_COORDENACAO = '//html/body/div/div[2]/form/table[1]/tbody/tr[28]/td'
PROJETO_XPATHS_CONTATO_EMAIL = '//html/body/div/div[2]/form/table[1]/tbody/tr[29]/td'
PROJETO_XPATHS_CONTATO_TELEFONE = '//html/body/div/div[2]/form/table[1]/tbody/tr[30]/td'