# selection_components.py
## @file
# Módulo com funções para interagir com a página da web e obter informações.

import components.selection_components as sc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.filter_descryption import *
from config.crawler_descryption import SEARCH_TYPES

def make_search(driver):
    """
    Realiza uma pesquisa utilizando um WebDriver específico.

    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    sc.use_element_by_id(NAME_BUTTON_BUSCAR, driver)

def get_error_message(driver):
    """
    Obtém a mensagem de erro da página da web.

    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Texto da mensagem de erro ou None se nenhuma mensagem de erro for encontrada.
    """
    try:
        return driver.find_element(By.XPATH, XPATH_ERROR_MESSAGE).text
    except:
        return None

def clear_input_name(name: str, driver):
    """
    Limpa o campo de entrada com o nome especificado.

    @param name: Atributo de nome do campo de entrada.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    input_field = driver.find_element(By.NAME, name)
    input_field.clear()

def uncheck_checkbox_name(name: str, driver):
    """
    Desmarca a caixa de seleção com o nome especificado.

    @param name: Atributo de nome da caixa de seleção.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    checkbox = driver.find_element(By.NAME, name)
    if checkbox.is_selected():
        checkbox.click()

def use_input_by_name(name: str, input: str, driver):
    """
    Interage com um campo de entrada usando seu nome.

    @param name: Atributo de nome do campo de entrada.
    @param input: Valor a ser inserido no campo.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    input_field = driver.find_element(By.NAME, name)
    input_field.click()
    input_field.send_keys(input)

def use_element_by_id(id: str, driver):
    """
    Interage com um elemento usando seu ID.

    @param id: Atributo de ID do elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    driver.find_element(By.ID, id).click()

def use_element_by_xpath(value: int, driver):
    """
    Interage com um elemento usando seu XPath.

    @param value: Expressão XPath para localizar o elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    driver.find_element(By.XPATH, value).click()

def use_element_by_class(class_name: str, driver):
    """
    Interage com um elemento usando seu nome de classe.

    @param class_name: Atributo de nome de classe do elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        element.click()
    except (TimeoutException, NoSuchElementException):
        return element

def get_element_by_id(id: str, driver):
    """
    Obtém um elemento pelo seu ID.

    @param id: Atributo de ID do elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Objeto WebElement representando o elemento localizado.
    """
    return driver.find_element(By.ID, id)

def get_element_by_xpath(value: str, driver):
    """
    Obtém um elemento pelo seu XPath.

    @param value: Expressão XPath para localizar o elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Objeto WebElement representando o elemento localizado.
    """
    return driver.find_element(By.XPATH, value)

def get_element_by_class(class_name: str, driver):
    """
    Obtém um elemento pelo seu nome de classe.

    @param class_name: Atributo de nome de classe do elemento.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Objeto WebElement representando o elemento localizado.
    """
    return driver.find_element(By.CLASS_NAME, class_name)

def get_element_by_select(name: str, option: str, driver):
    """
    Obtém um elemento pelo seu nome e seleciona uma opção de um menu suspenso.

    @param name: Atributo de nome do elemento (menu suspenso).
    @param option: Opção a ser selecionada no menu suspenso.
    @param driver: Objeto WebDriver para interagir com a página da web.
    """
    select = Select(driver.find_element_by_name(name))
    select.select_by_visible_text(option)

def get_rows_len(result_table):
    """
    Obtém o número de linhas em uma tabela.

    @param result_table: Objeto WebElement representando a tabela.
    @return: Número de linhas na tabela.
    """
    return len(result_table.find_elements(By.XPATH, ".//tr"))

def get_rows_from_table(driver):
    """
    Obtém o elemento da tabela da página da web.

    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Objeto WebElement representando a tabela.
    """
    try:
        table = WebDriverWait(driver, timeout=15).until(
            lambda driver: driver.find_element(By.ID, "listagem")
        )
        return table
    except NoSuchElementException:
        # Lidar com a exceção se o elemento da tabela não for encontrado
        return table

def count_listing(driver):
    """
    Conta o número de listagens na página da web.

    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Número de listagens.
    """
    try:
        rows = driver.find_elements(By.XPATH, XPATH_ROWS)
        return len(rows)
    except:
        return 0

def add_date_to_item(item, month, year):
    """
    Adiciona informações de data a um dicionário de item.

    @param item: Dicionário representando um item.
    @param month: Informações do mês a serem adicionadas.
    @param year: Informações do ano a serem adicionadas.
    @return: Dicionário de item atualizado com informações de data.
    """
    item['data_inicio'] = {'mes': month, 'ano': year}
    return item

def get_info_try_except(xpath, driver):
    """
    Obtém informações usando um bloco try-except com um XPath específico.

    @param xpath: Expressão XPath para localizar o elemento contendo informações.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Informações extraídas ou "N/A" se ocorrer uma exceção.
    """
    try:
        return get_element_by_xpath(xpath, driver).text
    except:
        return "N/A"

def get_info_directly(xpath, driver):
    """
    Obtém informações diretamente de um XPath específico.

    @param xpath: Expressão XPath para localizar o elemento contendo informações.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Informações extraídas.
    """
    return get_element_by_xpath(xpath, driver).text

def get_info(xpath, driver):
    """
    Obtém informações com base no tipo de pesquisa selecionado.

    @param xpath: Expressão XPath para localizar o elemento contendo informações.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Informações extraídas.
    """
    if SEARCH_TYPES == 'DIRECTLY':
        return get_info_directly(xpath, driver)
    elif SEARCH_TYPES == 'TRY_EXCEPT':
        return get_info_try_except(xpath, driver)

def get_qtd_tables_by_xpath(xpath, driver):
    """
    Obtém o número de tabelas em um formulário pelo seu XPath.

    @param xpath: Expressão XPath para localizar o formulário.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Número de tabelas no formulário.
    """
    form = driver.find_element(By.XPATH, xpath)
    return len(form.find_elements(By.XPATH, "table"))

def get_qtd_tables_by_xpath_relatorio(xpath, driver):
    """
    Obtém o número de tabelas em um formulário pelo seu XPath para um relatório.

    @param xpath: Expressão XPath para localizar o formulário.
    @param driver: Objeto WebDriver para interagir com a página da web.
    @return: Número de tabelas no formulário para um relatório.
    """
    form = driver.find_element(By.XPATH, xpath)
    return len(form.find_elements(By.XPATH, ".//tr"))
