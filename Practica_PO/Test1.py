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
        f = Funciones_Globales(driver) # en este caso no cumple ninguna función
        #f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", tg)
        #f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", tg)
        # f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", tg)
        f.Navegar("https://demoqa.com/text-box", tg)
        # f.Select_Xpath_Text("//select[contains(@id,'select-demo')]", "Sunday", tg)
        # f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", 'text', "Sunday", tg)
        # f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", 'value', "Friday", tg)
        # f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", 'index', "3", tg)
        # f.Select_ID_Type("select-demo", 'index', "3", tg)
        # f.Upload_Xpath("//input[contains(@id,'fileinput')]", "C://Users//HP//PycharmProjects//Curso_selenium1//Imagenes//demo1.jpg", tg)
        # f.Upload_ID("fileinput","C://Users//HP//PycharmProjects//Curso_selenium1//Imagenes//demo1.jpg", tg)
        #f.Check_Xpath("//input[contains(@id,'isAgeSelected')]", tg)
        # f.Check_ID("isAgeSelected", tg)
        # for n in range(2, 6):
        #    f.Check_xpath_multiple(tg, "(//input[contains(@type,'checkbox')])["+str(n)+"]")
        f.Texto_Mixto("id", "userName", "Camila", tg)
        f.Texto_Mixto("id", "userEmail", "cami.ga@gmail.com", tg)
        # f.Click_Mixto("id", "submit", tg)
        f.Click_Mixto("xpath", "//button[contains(@id,'submit')]", tg)



# funcion de cierre tear down
    def tearDown(self):
        driver = self.driver
        driver.close()

    if __name__ == '__main__':
        unittest.main()
