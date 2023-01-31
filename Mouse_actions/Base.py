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
from ..Funciones.funciones import Funciones_Globales
from selenium.webdriver import ActionChains

tg = 3

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://academia3e.com/courses/metodologias-agiles/", tg)
        icono = driver.find_element(By.ID, "Componente_29_12")
        sub1 = driver.find_element(By.XPATH, "//a[@href='https://academia3e.com/carrito'][contains(.,'VER MOCHILA')]")
        act = ActionChains(driver)
        act.move_to_element(icono).move_to_element(sub1).click().perform()
        time.sleep(tg)




    def tearDown(self):
        driver = self.driver
        driver.close()

    if __name__ == '__main__':
        unittest.main()