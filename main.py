from requeriments import checkLibraries 

class Main():
    def __init__(self):
        checkLibraries()
    def begin(self):
        from menu import Menu
        menu = Menu()
        menu.begin()

if __name__ == "__main__":
    main_obj = Main()
    main_obj.begin()