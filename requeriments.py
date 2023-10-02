import sys
import importlib
import subprocess
from config.libraries_descryption import list_libraries
from config.display_descryption import SEPARATOR, SLEEP_TIME
from config.crawler_descryption import SCHEDULE
import time

def checkLibraries():
    print(SEPARATOR)
    for library in list_libraries:
        try:
            importlib.import_module(library)
            print(f'{library} is installed')
        except ImportError:
            print(f'{library} is not installed')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            except Exception as e:
                print(f'Erro ao instalar {library} : {e}')
                exit(1)
    print(SEPARATOR)
    if SCHEDULE == True:
        time.sleep(SLEEP_TIME)
    else:
        input("Press enter to continue...")
