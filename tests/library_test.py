import unittest

class TestLibrary(unittest.TestCase):
    def testSelenium(self):
        try:
            import selenium
            has_request = True
        except ImportError:
            has_request = False
        self.assertTrue(has_request, "Selenium is not installed")

    def testDotenv(self):
        try:
            from dotenv import dotenv_values
            has_dotenv = True
        except ImportError:
            has_dotenv = False
        self.assertTrue(has_dotenv, "Dotenv is not installed")

    def testTqdm(self):
        try:
            from tqdm import tqdm
            has_tqdm = True
        except ImportError:
            has_tqdm = False
        self.assertTrue(has_tqdm, "Tqdm is not installed")

if __name__ == '__main__':
    unittest.main()