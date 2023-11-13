import unittest
import pages.sigaa_pages as sp
from concurrent.futures import ThreadPoolExecutor
from dotenv import dotenv_values # pip install python-dotenv
from selenium import webdriver
from tqdm import tqdm # pip install selenium
from config.crawler_descryption import MAX_THREADS, INVISIBLE
from config.url_descryption import *

from selenium.webdriver.chrome.service import Service

class TestCrawlerAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.username = None
        self.password = None

    def testGetCredentialsFromEnv(self):
        self.env = dotenv_values(".env")
        self.username = self.env['SIGAA_USER']
        self.password = self.env['SIGAA_PASS']
        self.assertIsNotNone(self.username)
        self.assertIsNotNone(self.password)
        self.assertNotEqual(self.username, '')
        self.assertNotEqual(self.password, '')

    def testLoginInstance(self):
        TestCrawlerAuth.testGetCredentialsFromEnv(self)

        self.driver.get(LOGIN_PAGE)
        self.assertEqual(self.driver.title, "STI : Autenticação Integrada")
        
        sp.login_into_sigaa(self.driver, self.username, self.password)
        
        self.driver.get(EXTENSION_PAGE)
        self.assertEqual(self.driver.title, "SIGAA - Sistema Integrado de Gestão de Atividades Acadêmicas")        

    def tearDown(self):
        self.driver.close()

class TestCrawlerAuthConcurrent(unittest.TestCase):
    def setUp(self):
        self.chrome_service = Service()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('headless') if INVISIBLE == True else self.chrome_options.add_argument('start-maximized')
        self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
        self.navegador = "chrome"

    def testGetCredentialsFromEnv(self):
        self.env = dotenv_values(".env")
        self.username = self.env['SIGAA_USER']
        self.password = self.env['SIGAA_PASS']
        self.assertIsNotNone(self.username)
        self.assertIsNotNone(self.password)
        self.assertNotEqual(self.username, '')
        self.assertNotEqual(self.password, '')

    def testLoginMultipleInstances(self):
        class MiniInstanceTest(TestCrawlerAuthConcurrent):
            def __init__(self, username, password):
                self.chrome_service = Service()
                self.chrome_options = webdriver.ChromeOptions()
                self.chrome_options.add_argument('headless') if INVISIBLE == True else self.chrome_options.add_argument('start-maximized')
                self.chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
                self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

                self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)
                self.username = username
                self.password = password
               
            def begin(self):
                self.driver.get(LOGIN_PAGE)
                login_title = self.driver.title

                sp.login_into_sigaa(self.driver, self.username, self.password)
                
                self.driver.get(EXTENSION_PAGE)
                extension_title = self.driver.title

                return login_title, extension_title
            
        TestCrawlerAuth.testGetCredentialsFromEnv(self)

        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            instances = [MiniInstanceTest(self.username, self.password).begin() for _ in tqdm(range(MAX_THREADS))]
        
        for instance in instances:
            login_title, extension_title = instance   
            
            self.assertEqual(login_title, "STI : Autenticação Integrada")
            self.assertEqual(extension_title, "SIGAA - Sistema Integrado de Gestão de Atividades Acadêmicas")        
           
if __name__ == '__main__':
    unittest.main()