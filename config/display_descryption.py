# display_descryption.py
## @file
# Módulo com as funções de exibição de informações no terminal.

import os

RIGHT_ARROW = "->"
LEFT_ARROW = "<-"
HASH = "#####"
SLEEP_TIME = 3
try:
    SIZE_TERMINAL = os.get_terminal_size().columns
except OSError as e:
    SIZE_TERMINAL = 70
SEPARATOR = "="*SIZE_TERMINAL

def centralize(msg:str):
    print(msg.center(SIZE_TERMINAL))

def clear_screen():
    if os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
        _ = os.system('clear')
    else:  # Para o Windows
        _ = os.system('cls')