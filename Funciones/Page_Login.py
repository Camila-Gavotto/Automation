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

class Pagina_Login():
    # nos sirve para inicializar todas las funciones
    def __init__(self, driver):
        self.driver = driver

    def Login_Master(self, url, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url, t)
        f.Texto_Xpath_validar("//input[contains(@id,'user-name')]", name, t)
        f.Texto_Xpath_validar("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_validar("//input[contains(@id,'login-button')]", t)
        f.Salida()
