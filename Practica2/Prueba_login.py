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

# iniciamos nuestra clase
class Test_Login (unittest.TestCase):

#función inicial
    def setUp(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        t = 2
        warnings.simplefilter('ignore', ResourceWarning)

    def test_login_1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        passw.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correctos")
            print("Prueba uno OK")
        time.sleep(3)

    def test_login_2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        passw.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba dos OK")
        time.sleep(3)


    def test_login_3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("Camila")
        passw.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Password is required"):
            print("Falta la contraseña")
            print("Prueba tres OK")
        time.sleep(3)

    def test_login_4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        passw.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)
        if (error == "Epic sadface: Username is required"):
            print("Faltan los dos campos")
            print("Prueba cuatro pendiente")
        time.sleep(3)

    def test_login_5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH,"//input[contains(@id,'user-name')]")
        passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        passw.send_keys("secret_sauce")
        btn.click()
        element = driver.find_element(By.XPATH, "//div[contains(@class,'app_logo')]")
        print("El elemento es: ", element)
        print("Prueba cinco OK")
        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__' :
    unittest.main()
