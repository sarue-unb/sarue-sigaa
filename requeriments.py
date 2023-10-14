import importlib
import subprocess
import sys

from config.libraries_descryption import list_libraries
from config.display_descryption import SEPARATOR, SLEEP_TIME
from config.crawler_descryption import SCHEDULE

def update_library(library_name, library_import):
    try:
        importlib.import_module(library_name)
        print(f'{library_name} is installed')
        print(f'Updating {library_name} to the latest version...')
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_import, "-U"])
        print(f'{library_name} has been updated to the latest version.')

    except ImportError:
        print(f'{library_name} is not installed')
        print(f'Installing {library_name}...')
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library_import])
            print(f'{library_name} has been installed.')
        except Exception as e:
            print(f'Error installing {library_name}: {e}')
            sys.exit(1)

    except Exception as e:
        print(f'Error updating {library_name}: {e}')

def checkLibraries():
    print(SEPARATOR)
    for library_name, library_import in list_libraries.items():
        update_library(library_name, library_import)
    print(SEPARATOR)

    if SCHEDULE:
        import time
        time.sleep(SLEEP_TIME)
    else:
        input("Press enter to continue...")