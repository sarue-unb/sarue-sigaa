import sys

args = sys.argv
type_base = args[1].upper()

if type_base == 'BASE':
    START_YEAR = 2023
    END_YEAR = 2023
elif type_base == 'REBASE':
    START_YEAR = 2020
    END_YEAR = 2022

FIRST_MONTH_OF_YEAR = 1
LAST_MONTH_OF_YEAR = 12

SPECIAL_DATE = ['9/2023', '3/2023', '8/2022', '9/2021']

FIRST_DAY_OF_MONTH = '01'

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