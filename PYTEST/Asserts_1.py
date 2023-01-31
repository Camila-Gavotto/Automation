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
"""
@pytest.mark.validarif
def test_validar_if():
    nom1 = "Camila"
    nom2 = "Camila"

    assert nom1 == nom2, "Los nombres no son iguales"


@pytest.mark.validarif
def test_validar_if():
    dato = "computadoras"
    frase = "Dentro de la computadora hay memoria RAM"

    assert dato in frase, "El dato no esta dentro de la frase"

"""
@pytest.mark.validarif
def test_validar_if():
    a= 20
    b= 20
    if(a==b):
        assert True, "Los datos son iguales"
    else:
        assert False, "No son iguales"