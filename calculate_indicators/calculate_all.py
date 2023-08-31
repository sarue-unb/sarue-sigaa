from config.json_descryption import OUTPUT_NAMES
from database_generator.load_database import add_item_to_indicators_database

from calculate_indicators.calculate_qtd import *
from calculate_indicators.calculate_status import *
from calculate_indicators.calculate_objectives import *
from calculate_indicators.calculate_members import *

def calculate_all_indicators(origin_database: dict):
    # Indicadores de quantidade de ações
    actions_month, actions_month_type, actions_year, actions_year_type = get_qtd_actions(origin_database)
  
    add_item_to_indicators_database("quantidade_anual", actions_year, "quantidades")
    add_item_to_indicators_database("quantidade_anual_tipo", actions_year_type, "quantidades")
    add_item_to_indicators_database("quantidade_mensal", actions_month, "quantidades")
    add_item_to_indicators_database("quantidade_mensal_tipo", actions_month_type, "quantidades")
    
    # Indicadores de status das ações
    actions_status_month, actions_status_month_type, actions_status_year, actions_status_year_type = get_qtd_actions_status(origin_database)

    add_item_to_indicators_database("status_acao_anual", actions_status_year, "status_acao")
    add_item_to_indicators_database("status_acao_anual_tipo", actions_status_year_type, "status_acao")
    add_item_to_indicators_database("status_acao_mensal", actions_status_month, "status_acao")
    add_item_to_indicators_database("status_acao_mensal_tipo", actions_status_month_type, "status_acao")

    # Indicadores de objetivos contemplados
    actions_objectives, actions_objectives_month, actions_objectives_month_type, actions_objectives_year, actions_objectives_year_type = get_qtd_actions_objectives(origin_database)

    add_item_to_indicators_database("objetivos_contemplados", actions_objectives, "objetivos")
    add_item_to_indicators_database("objetivos_contemplados_anual", actions_objectives_year, "objetivos")
    add_item_to_indicators_database("objetivos_contemplados_anual_tipo", actions_objectives_year_type, "objetivos")
    add_item_to_indicators_database("objetivos_contemplados_mensal", actions_objectives_month, "objetivos")
    add_item_to_indicators_database("objetivos_contemplados_mensal_tipo", actions_objectives_month_type, "objetivos")

    # Indicadores de quantidade de objetivos contemplados
    qtd_actions_objectives, qtd_actions_objectives_month, qtd_actions_objectives_month_type, qtd_actions_objectives_year, qtd_actions_objectives_year_type = get_qtd_actions_objectives_len(origin_database)

    add_item_to_indicators_database("quantidade_objetivos_contemplados", qtd_actions_objectives, "objetivos")
    add_item_to_indicators_database("quantidade_objetivos_contemplados_anual", qtd_actions_objectives_year, "objetivos")
    add_item_to_indicators_database("quantidade_objetivos_contemplados_anual_tipo", qtd_actions_objectives_year_type, "objetivos")
    add_item_to_indicators_database("quantidade_objetivos_contemplados_mensal", qtd_actions_objectives_month, "objetivos")
    add_item_to_indicators_database("quantidade_objetivos_contemplados_mensal_tipo", qtd_actions_objectives_month_type, "objetivos")
   
    qtd_members, qtd_members_month, qtd_members_month_type, qtd_members_year, qtd_members_year_type, members, members_month, members_month_type, members_year, members_year_type = get_qtd_actions_members_role(origin_database)

    add_item_to_indicators_database("quantidade_envolvidos", qtd_members, "envolvidos")
    add_item_to_indicators_database("quantidade_envolvidos_anual", qtd_members_year, "envolvidos")
    add_item_to_indicators_database("quantidade_envolvidos_mensal", qtd_members_month, "envolvidos")
    add_item_to_indicators_database("quantidade_envolvidos_anual_tipo", qtd_members_year_type, "envolvidos")
    add_item_to_indicators_database("quantidade_envolvidos_mensal_tipo", qtd_members_month_type, "envolvidos")

    add_item_to_indicators_database("envolvidos", members, "envolvidos")
    add_item_to_indicators_database("envolvidos_anual", members_year, "envolvidos")
    add_item_to_indicators_database("envolvidos_mensal", members_month, "envolvidos")
    add_item_to_indicators_database("envolvidos_anual_tipo", members_year_type, "envolvidos")
    add_item_to_indicators_database("envolvidos_mensal_tipo", members_month_type, "envolvidos")

    actions_information, actions_information_month, actions_information_month_type, actions_information_year, actions_information_year_type = get_qtd_info(origin_database)

    add_item_to_indicators_database("info", actions_information, "info_acoes")
    add_item_to_indicators_database("info_anual", actions_information_year, "info_acoes")   
    add_item_to_indicators_database("info_mensal", actions_information_month, "info_acoes")
    add_item_to_indicators_database("info_anual_tipo", actions_information_year_type, "info_acoes")
    add_item_to_indicators_database("info_mensal_tipo", actions_information_month_type, "info_acoes")