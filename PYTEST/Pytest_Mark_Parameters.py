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


def get_Data():
    return [
        ("Camila", "1234"),
        ("juan", "123334"),
        ("Rodrigo", "12322344"),
        ("Pedro", "1534ff234"),
        ("Enzo", "125gg534"),
        ("Admin", "admin123")
    ]


@pytest.mark.login
@pytest.mark.parametrize("user, clave", get_Data())
def test_Login(user, clave):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[@name='username']", user, t)
    f.Texto_Mixto("xpath", "//input[@type='password']", clave, t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)

def teardown_function():
    print("Salida del test")
    driver.close()


