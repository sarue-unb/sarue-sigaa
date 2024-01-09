# requirements.py

## @file
# Módulo para verificar e atualizar bibliotecas necessárias.

import importlib
import subprocess
import sys

from config.libraries_descryption import list_libraries
from config.display_descryption import SEPARATOR, SLEEP_TIME
from config.crawler_descryption import SCHEDULE

## Função para verificar a instalação do pip e atualizá-lo, se necessário.
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

## Função para verificar e atualizar uma biblioteca específica.
# @param library_name Nome da biblioteca.
# @param library_import Nome da biblioteca para importação.
def update_library(library_name, library_import):
    try:
        importlib.import_module(library_name)
        print(f'{library_name} está instalada')
        print(f'Atualizando {library_name} para a versão mais recente...')
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_import, "-U"])
        print(f'{library_name} foi atualizada para a versão mais recente.')

    except ImportError:
        print(f'{library_name} não está instalada')
        print(f'Instalando {library_name}...')
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library_import])
            print(f'{library_name} foi instalada.')
        except Exception as e:
            print(f'Erro ao instalar {library_name}: {e}')
            sys.exit(1)

    except Exception as e:
        print(f'Erro ao atualizar {library_name}: {e}')

## Função principal para verificar e atualizar todas as bibliotecas necessárias.
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
        input("Pressione Enter para continuar...")
