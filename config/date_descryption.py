from config.crawler_descryption import TYPE_BASE

START_YEAR = 2023 if TYPE_BASE == 'BASE' else 2020
END_YEAR = 2023 if TYPE_BASE == 'BASE' else 2022

FIRST_MONTH_OF_YEAR = 1
LAST_MONTH_OF_YEAR = 12

SPECIAL_DATE = ['9/2023', '3/2023', '8/2022', '9/2021']

FIRST_DAY_OF_MONTH = '01'

EMPTY_MONTH = '1/2020' #used for offset and test
HAS_DATA_MONTH = '7/2022' #used for test

LEAP_YEAR = [2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]

MONTHS_LAST_DAY = {
    1: '31',
    2: '28',
    3: '31',
    4: '30',
    5: '31',
    6: '30',
    7: '31',
    8: '31',
    9: '30',
    10: '31',
    11: '30',
    12: '31',
}

DIGITS_MONTHS = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'março',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}