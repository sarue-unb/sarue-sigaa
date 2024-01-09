# calculate_functions.py
## @file
# Módulo com funções auxiliares para o cálculo dos indicadores.

import re

def create_dictionary_place(indicators: dict, key: str, value: int) -> dict:
    """
    Cria uma entrada de dicionário ou atualiza o valor se a chave já existir.

    @param indicators: Dicionário de entrada.
    @param key: Chave para a entrada do dicionário.
    @param value: Valor a ser associado à chave.
    @return: Dicionário atualizado.
    """

    if key not in indicators:
        indicators[key] = value

def create_set_place(indicators: dict, key: str, value: int) -> dict:
    """
    Cria uma entrada de conjunto ou adiciona o valor a um conjunto existente para a chave especificada.

    @param indicators: Dicionário de entrada.
    @param key: Chave para a entrada do conjunto.
    @param value: Valor a ser adicionado ao conjunto.
    @return: Dicionário atualizado com uma entrada de conjunto.
    """

    if key not in indicators:
        indicators[key] = set()
    indicators[key].add(value)

def update_dictionary_place(indicators: dict, key: str, value: int) -> dict:
    """
    Atualiza uma entrada do dicionário adicionando o valor especificado ao valor existente para a chave.

    @param indicators: Dicionário de entrada.
    @param key: Chave para a entrada do dicionário.
    @param value: Valor a ser adicionado ao valor existente.
    @return: Dicionário atualizado.
    """

    if key not in indicators:
        indicators[key] = value
    else:
        indicators[key] += value

    return indicators

def return_number(text: str) -> int:
    """
    Extrai e retorna o primeiro inteiro encontrado no texto de entrada.

    @param text: Texto de entrada contendo valores numéricos.
    @return: Inteiro extraído ou 0 se nenhum inteiro for encontrado.
    """

    pattern = r'(\d+)'
    result = re.search(pattern, text)  # Search for the pattern in the text

    if result:
        return int(result.group(1))  # Convert the found value to an integer
    else:
        return 0
