# Main.py

## @file
# Arquivo principal responsável por inicializar e iniciar o programa.

from requeriments import checkLibraries 
from config.display_descryption import clear_screen

## Classe principal responsável pela inicialização e execução do programa.
class Main():
    ## Método construtor da classe Main.
    def __init__(self):
        ## Limpa a tela do terminal usando a função clear_screen.
        clear_screen()
        ## Verifica se as bibliotecas necessárias estão instaladas usando a função checkLibraries.
        checkLibraries()

    ## Método para iniciar o programa.
    def begin(self):
        ## Importa a classe Menu do módulo menu.
        from menu import Menu
        ## Cria uma instância da classe Menu.
        menu = Menu()
        ## Invoca o método begin da classe Menu para iniciar o programa.
        menu.begin()

## Bloco de execução principal.
if __name__ == "__main__":
    ## Cria uma instância da classe Main.
    main_obj = Main()
    ## Inicia o programa invocando o método begin da classe Main.
    main_obj.begin()
