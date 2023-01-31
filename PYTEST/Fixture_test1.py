import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from funciones import Funciones_Globales
from Page_Login import Funciones_Login
t = .1
driver = ""
f = ""

def setup_function(function):
    global driver, f # variable global para usarlo en todos lados
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Iniciando nuestros test")


def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchProductName')]", "computer", t)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-products')]", t)

def test_dos():
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath", "//a[@href='/Admin/Product/Create']", t)
    f.Texto_Mixto("xpath", "//input[@id='Name']", "Laptop Dell", 4)
    f.Texto_Mixto("xpath", "//textarea[contains(@id,'ShortDescription')]", "Laptop modelo nuevo tipo Dell", 4)
    f.Click_Mixto("xpath", "//span[@class='tox-mbtn__select-label'][contains(.,'File')]", t)
    f.Click_Mixto("xpath", "//div[@class='tox-collection__item-label'][contains(.,'New document')]", t)
    driver.switch_to.frame(0)
    campo = driver.find_element(By.ID, "tinymce")
    campo.send_keys("Descripción larga" + Keys.TAB + "12342")
    time.sleep(2)