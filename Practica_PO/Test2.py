import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.funciones import Funciones_Globales
from Funciones.Page_Login import Pagina_Login

tg = 2

# iniciamos nuestra clase
class base_test(unittest.TestCase):

# función inicial
    def setUp(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        warnings.simplefilter('ignore', ResourceWarning)


    def test_1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        f.Texto_Mixto("id", "userName", "Camila", tg)
        f.Texto_Mixto("id", "userEmail", "cami@gmail.com", tg)
        f.Texto_Mixto("id", "currentAddress", "Demo uno de texto para pruebas", tg)
        f.Texto_Mixto("id", "permanentAddress", "Demo uno de texto para pruebas", tg)
        f.Click_Mixto("id", "submit", tg)


# funcion de cierre tear down
    def tearDown(self):
        driver = self.driver
        driver.close()

    if __name__ == '__main__':
        unittest.main()