import unittest
from selenium import webdriver
from config.url_descryption import *
import components.selection_components as sc
import pages.sigaa_pages as sp 

class TestUrl(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testMainPage(self):
        self.driver.get(MAIN_PAGE)
        self.assertEqual(self.driver.title, "STI : Autenticação Integrada")

    def testLoginPage(self):
        self.driver.get(LOGIN_PAGE)
        self.assertEqual(self.driver.title, "STI : Autenticação Integrada")
    
    def testUsername(self):
        self.driver.get(LOGIN_PAGE)
        sc.get_element_by_xpath(sp.USERNAME_XPATH, self.driver)
        
    def testPassword(self):
        self.driver.get(LOGIN_PAGE)
        sc.get_element_by_xpath(sp.PASSWORD_XPATH, self.driver)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()