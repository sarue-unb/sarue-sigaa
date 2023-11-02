import importlib
import subprocess
import sys

from config.libraries_descryption import list_libraries
from config.display_descryption import SEPARATOR, SLEEP_TIME
from config.crawler_descryption import SCHEDULE

def check_install_pip():
    try:
        # Verificar se o pip está instalado
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        # Se o pip não estiver instalado, tentar instalá-lo com apt (para sistemas baseados em Debian)
        try:
            subprocess.check_call(['sudo', 'apt', 'install', 'python3-pip'])
        except subprocess.CalledProcessError as e:
            print("Erro ao tentar instalar pip:", e)
    else:
        # Se o pip estiver instalado, atualizar para a versão mais recente
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pip", "-U"])
        except subprocess.CalledProcessError as e:
            print("Erro ao tentar atualizar o pip:", e)

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
    check_install_pip()
    print(SEPARATOR)
    for library_name, library_import in list_libraries.items():
        update_library(library_name, library_import)
    print(SEPARATOR)

    if SCHEDULE:
        import time
        time.sleep(SLEEP_TIME)
    else:
        input("Press enter to continue...")