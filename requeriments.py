import sys
import importlib
import subprocess
from config.libraries_descryption import list_libraries

def checkLibraries():
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
    input("Press enter to continue...")
