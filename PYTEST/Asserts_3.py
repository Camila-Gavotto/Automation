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

@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[@name='username']", "Admin", t)
    f.Texto_Mixto("xpath", "//input[@type='password']", "admin123", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("Entrando al sistema")

def teardown_function():
    print("Fin de todos los Test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    etiqueta = f.SEX("//h6[contains(.,'Dashboard')]").text
    if(etiqueta=="Dashboard"):
        print("Adentro")
        assert etiqueta == "Dashboard"
    else:
        print("Afuera")
        assert etiqueta == "Dashboard", "No estas en la página de inicio"
