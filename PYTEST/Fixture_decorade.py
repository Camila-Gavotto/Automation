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
def setup_login_uno():
    print("Empezando el login del sistema uno")
    yield # es como el turndown
    print("Fin de las pruebas del sistema uno")

@pytest.fixture(scope = 'module') # estos son decoradores y setup login dos es la palabra que utilizamos p ese decorador
def setup_login_dos():
    print("Empezando las pruebas del sistema dos")
    yield
    print("Fin de las pruebas del sistema dos")


def test_uno(setup_login_uno):
    print("#######Empezando las pruebas del test 1#########")

def test_dos(setup_login_dos):
    print("Esto es para la prueba dos")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("Prueba tres del modulo login 2")
    