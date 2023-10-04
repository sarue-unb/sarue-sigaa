import importlib
import unittest
from config.libraries_descryption import list_libraries

class TestLibrary(unittest.TestCase):
    def testLibraries(self):
        for library_name, library_import in list_libraries.items():
            try:
                importlib.import_module(library_name)
                has_library = True
            except ImportError:
                has_library = False
            self.assertTrue(has_library, f"{library_import} is not installed")

if __name__ == '__main__':
    unittest.main()