import re

def create_dictionary_place(indicators:dict, key:str, value:int) -> dict:
    if key not in indicators:
        indicators[key] = value

def create_set_place(indicators:dict, key:str, value:int) -> dict:
    if key not in indicators:
        indicators[key] = set()
    indicators[key].add(value)

def update_dictionary_place(indicators:dict, key:str, value:int) -> dict:
    if key not in indicators:
        indicators[key] = value
    else:
        indicators[key] += value

    return indicators

def return_number(text: str) -> int:
    padrao = r'(\d+)'
    resultado = re.search(padrao, text)  # Procurar o padrão no texto

    if resultado:
        return int(resultado.group(1))  # Converter o valor encontrado para um inteiro
    else:
        return 0
    