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

tg = 2


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("http://testpages.herokuapp.com/styled/drag-drop-javascript.html", tg)
        f.Mouse_DragAndDrop("xpath", "//div[contains(@id,'draggable1')]", "//div[contains(@id,'droppable1')]", tg)
        f.Mouse_DragAndDrop("xpath", "//div[contains(@id,'draggable2')]", "//div[contains(@id,'droppable1')]", tg)



    def tearDown(self):
        driver = self.driver
        driver.close()

    if __name__ == '__main__':
        unittest.main()