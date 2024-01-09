# json_descryption.py
## @file
# Nome do arquivo JSON contendo o banco de dados base.

FILE_PATH = "databases/"

FILE_PATH_BASE = 'base/'
FILE_PATH_CURRENT = 'current/'
FILE_PATH_HISTORY = 'history/'
FILE_PATH_INDICATORS = 'indicators/'
FILE_PATH_OUTPUTS = 'outputs/'

FILE_NAME_BASE = "base.json"
FILE_NAME_CURRENT = "current_output_file.json"
FILE_NAME_FULL = "full_database.json"
FILE_NAME_HISTORY = "db_activities_"
FILE_NAME_EXCEL = "current_output_file.xlsx"

FILE_NAME_BASE_DATABASE = FILE_PATH + FILE_PATH_BASE + FILE_NAME_BASE
FILE_NAME_CURRENT_DATABASE = FILE_PATH + FILE_PATH_CURRENT + FILE_NAME_CURRENT
FILE_NAME_FULL_DATABASE = FILE_PATH + FILE_PATH_INDICATORS + FILE_NAME_FULL
FILE_NAME_HISTORY_DATABASE = FILE_PATH + FILE_PATH_HISTORY + FILE_NAME_HISTORY
FILE_NAME_EXCEL_DATABASE = FILE_PATH + FILE_PATH_OUTPUTS + FILE_NAME_EXCEL

INDICATORS_NAMES = {
    "quantidades" : "quantidades/",
    "status_acao" : "status_acao/",
    "objetivos" : "objetivos/",
    "envolvidos" : "envolvidos/",
    "info_acoes" : "info_acoes/",
}

OUTPUT_NAMES = {
    "quantidades" : {
        "quantidade" : {},
        "quantidade_anual" : {},
        "quantidade_mensal" : {},
        "quantidade_anual_tipo" : {},
        "quantidade_mensal_tipo" : {},
    },
    "status_acao" : {
        "status_acao" : {},
        "status_acao_anual" : {},
        "status_acao_mensal" : {},
        "status_acao_anual_tipo" : {},
        "status_acao_mensal_tipo" : {},
    },
    "objetivos" : {
        "objetivos_contemplados" : {},
        "objetivos_contemplados_anual" : {},
        "objetivos_contemplados_mensal" : {},
        "objetivos_contemplados_anual_tipo" : {},
        "objetivos_contemplados_mensal_tipo" : {},
        "quantidade_objetivos_contemplados" : {},
        "quantidade_objetivos_contemplados_anual" : {},
        "quantidade_objetivos_contemplados_mensal" : {},
        "quantidade_objetivos_contemplados_anual_tipo" : {},
        "quantidade_objetivos_contemplados_mensal_tipo" : {},
    },
    "envolvidos" : {
        "quantidade_envolvidos" : {},
        "quantidade_envolvidos_anual" : {},
        "quantidade_envolvidos_mensal" : {},
        "quantidade_envolvidos_anual_tipo" : {},
        "quantidade_envolvidos_mensal_tipo" : {},
        "envolvidos" : {},
        "envolvidos_anual" : {},
        "envolvidos_mensal" : {},
        "envolvidos_anual_tipo" : {},
        "envolvidos_mensal_tipo" : {},
    },
    "info_acoes" : {
        "info" : {},
        "info_anual" : {},
        "info_mensal" : {},
        "info_anual_tipo" : {},
        "info_mensal_tipo" : {},
    },
}