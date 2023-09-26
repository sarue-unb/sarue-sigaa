import os

RIGHT_ARROW = "->"
LEFT_ARROW = "<-"
HASH = "#####"
SIZE_TERMINAL = os.get_terminal_size().columns
SEPARATOR = "="*SIZE_TERMINAL

def centralize(msg:str):
    print(msg.center(SIZE_TERMINAL))

def clear_screen():
    if os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
        _ = os.system('clear')
    else:  # Para o Windows
        _ = os.system('cls')