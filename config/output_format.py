import os
import re
import time
from database_generator.json_generator import get_quantity_of_activities
from config.display_descryption import *

FORMATER = r'[0-9]+|[^\w\s]'

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

        clear_screen()
        centralize(f'{RIGHT_ARROW} Script end {LEFT_ARROW}')

        print(SEPARATOR)
        centralize(f'Quantidade de ações = {get_quantity_of_activities()}')
        print(SEPARATOR)

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

def clear_strings(text: str) -> str:
    return re.sub(FORMATER, '', text)

def clear_log():
    with open('log.txt', 'w+') as file:
        file.write('')

def add_item_to_log(item:str):
    with open('log.txt', 'a') as file:
        file.write(item + '\n')