from requeriments import checkLibraries 
from config.display_descryption import clear_screen

class Main():
    def __init__(self):
        clear_screen()
        checkLibraries()
    def begin(self):
        from menu import Menu
        menu = Menu()
        menu.begin()

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()