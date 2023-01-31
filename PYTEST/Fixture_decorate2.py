import time
import allure
import pytest
from allure_commons.types import AttachmentType
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

# Para imágenes de Error

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f  # variable global para usarlo en todos lados
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Entrando al sistema")
    yield
    print("Salida del login uno")



@pytest.fixture(scope='module')
def setup_login_dos():
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
    yield
    print("Salida del login dos")

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[2]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchFirstName')]", "victoria", t)
    allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-customers')]", 2)
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)
    # Creando un nuevo usuario
    f.Click_Mixto("xpath", "//a[@href='/Admin/Customer/Create']", t)
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.send_keys("juan@gmail.com" + Keys.TAB + "12345" + Keys.TAB + "Juan" + Keys.TAB + "Perez")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//input[contains(@id,'Gender_Male')]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'DateOfBirth')]", "02/20/2000", 4)
    assert 1==2
    driver.close()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")
    f.Click_Mixto("xpath", "//a[contains(.,'Admin')]", t)
    f.Click_Mixto("xpath", "(//span[contains(.,'User Management')])[2]", t)
    allure.attach(driver.get_screenshot_as_png(), name="Menu_admin", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "(//li[contains(.,'Users')])[2]", t)
    f.Texto_Mixto("xpath", "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input", "Admin", 1)
    assert 1==2
    driver.close()