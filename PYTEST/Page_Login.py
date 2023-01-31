import time
import pytest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from funciones import Funciones_Globales

class Funciones_Login():

    def __init__(self, driver):
        self.driver = driver

    def L1(self, email, clave, mensaje, t=.1):
        driver = webdriver.Chrome()
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        er1 = f.SEX("//li[contains(.,'No customer account found')]")
        er1 = er1.text
        if (er1 == mensaje):
            print("El Error arrojado es el correcto")
        else:
            print("El Error arrojado es incorrecto")
        driver.close()

    def L2(self, email, clave, mensaje, t=.1):
        driver = webdriver.Chrome()
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e2 = f.SEX("//span[contains(@id,'Email-error')]")
        e2 = e2.text
        print(e2)
        if (e2 == mensaje):
            print("Prueba de Email Vacio Exitosa")
        else:
            print("La Prueba de Email Vacio Rechazada")
        driver.close()

    def L3(self,email, clave, mensaje, t=.1):
        driver = webdriver.Chrome()
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        # ingresamos datos incorrectos y validamos el error
        e3 = f.SEX("//span[contains(@id,'Email-error')]")
        e3 = e3.text
        # print(e3)
        if (e3 == mensaje):
            print("Email no valido Prueba exitosa")
        else:
            print("La Prueba de Email Rechazada")
        driver.close()

    def L4(self, email, clave, mensaje, t=.1):
        driver = webdriver.Chrome()
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        f.Texto_Mixto("id", "Email", email, t)
        f.Texto_Mixto("id", "Password", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        # ingresamos datos incorrectos y validamos el error
        e4 = f.SEX("//h1[contains(.,'Dashboard')]")
        e4 = e4.text
        # print(e4)
        if (e4 == mensaje):
            print("Login exitoso")
        else:
            print("Login incorrecto")
        driver.close()