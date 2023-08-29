from config.json_descryption import OUTPUT_NAMES
from database_generator.load_database import add_item_to_indicators_database

from calculate_indicators.calculate_qtd import *
from calculate_indicators.calculate_status import *
from calculate_indicators.calculate_objectives import *
from calculate_indicators.calculate_members import *

def calculate_all_indicators(origin_database: dict):
    # Indicadores de quantidade de ações
    actions_month, actions_month_type, actions_year, actions_year_type = get_qtd_actions(origin_database)
  
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_anual"], actions_year, OUTPUT_NAMES["quantidade_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_mensal"], actions_month, OUTPUT_NAMES["quantidade_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_anual_tipo"], actions_year_type, OUTPUT_NAMES["quantidade_anual_tipo"])   
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_mensal_tipo"], actions_month_type, OUTPUT_NAMES["quantidade_mensal_tipo"])
    
    # Indicadores de status das ações
    actions_status_month, actions_status_month_type, actions_status_year, actions_status_year_type = get_qtd_actions_status(origin_database)

    add_item_to_indicators_database(OUTPUT_NAMES["status_acao_anual"], actions_status_year, OUTPUT_NAMES["status_acao_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["status_acao_anual_tipo"], actions_status_year_type, OUTPUT_NAMES["status_acao_anual_tipo"])
    add_item_to_indicators_database(OUTPUT_NAMES["status_acao_mensal"], actions_status_month, OUTPUT_NAMES["status_acao_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["status_acao_mensal_tipo"], actions_status_month_type, OUTPUT_NAMES["status_acao_mensal_tipo"])

    # Indicadores de objetivos contemplados
    actions_objectives_month, actions_objectives_month_type, actions_objectives_year, actions_objectives_year_type = get_qtd_actions_objectives(origin_database)

    add_item_to_indicators_database(OUTPUT_NAMES["objetivos_contemplados_anual"], actions_objectives_year, OUTPUT_NAMES["objetivos_contemplados_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["objetivos_contemplados_anual_tipo"], actions_objectives_year_type, OUTPUT_NAMES["objetivos_contemplados_anual_tipo"])
    add_item_to_indicators_database(OUTPUT_NAMES["objetivos_contemplados_mensal"], actions_objectives_month, OUTPUT_NAMES["objetivos_contemplados_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["objetivos_contemplados_mensal_tipo"], actions_objectives_month_type, OUTPUT_NAMES["objetivos_contemplados_mensal_tipo"])

    # Indicadores de quantidade de objetivos contemplados
    qtd_actions_objectives_month, qtd_actions_objectives_month_type, qtd_actions_objectives_year, qtd_actions_objectives_year_type = get_qtd_actions_objectives_len(origin_database)

    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_objetivos_contemplados_anual"], qtd_actions_objectives_year, OUTPUT_NAMES["quantidade_objetivos_contemplados_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_objetivos_contemplados_anual_tipo"], qtd_actions_objectives_year_type, OUTPUT_NAMES["quantidade_objetivos_contemplados_anual_tipo"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_objetivos_contemplados_mensal"], qtd_actions_objectives_month, OUTPUT_NAMES["quantidade_objetivos_contemplados_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_objetivos_contemplados_mensal_tipo"], qtd_actions_objectives_month_type, OUTPUT_NAMES["quantidade_objetivos_contemplados_mensal_tipo"])
   
    qtd_members, qtd_members_month, qtd_members_month_type, qtd_members_year, qtd_members_year_type, members, members_month, members_month_type, members_year, members_year_type = get_qtd_actions_members_role(origin_database)

    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_envolvidos"], qtd_members, OUTPUT_NAMES["quantidade_envolvidos"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_envolvidos_anual"], qtd_members_year, OUTPUT_NAMES["quantidade_envolvidos_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_envolvidos_anual_tipo"], qtd_members_year_type, OUTPUT_NAMES["quantidade_envolvidos_anual_tipo"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_envolvidos_mensal"], qtd_members_month, OUTPUT_NAMES["quantidade_envolvidos_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["quantidade_envolvidos_mensal_tipo"], qtd_members_month_type, OUTPUT_NAMES["quantidade_envolvidos_mensal_tipo"])

    add_item_to_indicators_database(OUTPUT_NAMES["envolvidos"], members, OUTPUT_NAMES["envolvidos"])
    add_item_to_indicators_database(OUTPUT_NAMES["envolvidos_anual"], members_year, OUTPUT_NAMES["envolvidos_anual"])
    add_item_to_indicators_database(OUTPUT_NAMES["envolvidos_anual_tipo"], members_year_type, OUTPUT_NAMES["envolvidos_anual_tipo"])
    add_item_to_indicators_database(OUTPUT_NAMES["envolvidos_mensal"], members_month, OUTPUT_NAMES["envolvidos_mensal"])
    add_item_to_indicators_database(OUTPUT_NAMES["envolvidos_mensal_tipo"], members_month_type, OUTPUT_NAMES["envolvidos_mensal_tipo"])