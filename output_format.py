RIGHT_ARROW = "->"
LEFT_ARROW = "<-"
HASH = "#####"
SIZE_TERMINAL = 70
SEPARATOR = "="*SIZE_TERMINAL

import time
import os

class Timer:
    def __init__(self) -> None:
        self.start_time = time.time()
        self.start_ctime = time.ctime()

    def set_start_time(self):
        self.start_time = time.time()
        self.start_ctime = time.ctime()

    def set_end_time(self):
        self.end_time = time.time()
        self.end_ctime = time.ctime()

    def get_elapsed_time(self):
        self.set_end_time()
        elapsed_time = (self.end_time - self.start_time)
        minutes = int(elapsed_time/60)
        seconds = int(elapsed_time%60)

        return minutes, seconds
    
    def print_elapsed_ctime(self):
        self.set_end_time()
        minutes, seconds = self.get_elapsed_time()

        centralize(f'{RIGHT_ARROW} Script end {LEFT_ARROW}')
        print(SEPARATOR)
        print(f"\tStart time: {self.start_ctime}")
        print(f"\tEnd time: {self.end_ctime}")
        print(f"\tElapsed time: {minutes:02}:{seconds:02} minutes")
        print(SEPARATOR)

    def print_partial_elapsed_ctime(self, msg:str):
        self.set_end_time()
        minutes, seconds = self.get_elapsed_time()

        print(SEPARATOR)
        print(f"{msg} - {minutes:02}:{seconds:02}")
        print(SEPARATOR)


def centralize(msg:str):
    print(msg.center(SIZE_TERMINAL))

def clear_screen():
    if os.name == 'posix':  # Para sistemas Unix (Linux, macOS)
        _ = os.system('clear')
    else:  # Para o Windows
        _ = os.system('cls')
