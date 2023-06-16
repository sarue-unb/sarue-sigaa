RIGHT_ARROW = " -> "
LEFT_ARROW = " <- "
HASH = " ##### "

pages_valid = {
    'discente' : ["https://sigaa.unb.br/sigaa/portais/discente/discente.jsf", "https://sigaa.unb.br/sigaa/telaAvisoLogon.jsf"],
    'docente' : ["https://sigaa.unb.br/sigaa/portais/docente/docente.jsf"]
}

import time

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
        return (self.end_time - self.start_time)/60
    
    def print_elapsed_ctime(self):
        self.set_end_time()
        print("Script end")
        print(f"\tStart time: {self.start_ctime}")
        print(f"\tEnd time: {self.end_ctime}")
        print(f"\tElapsed time: {self.get_elapsed_time():.2f} minutes")
