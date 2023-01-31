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
from selenium.webdriver import ActionChains

class Funciones_Globales():
    # nos sirve para inicializar todas las funciones
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: ", Url)
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t

    def Click_Mixto(self, tipo, selector, tiempo):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("Damos click en el botón {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("Damos click en el botón {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t


    def Salida(self):
        print("Se termina la prueba exitosamente")


    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = self.SEX(xpath)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print("El campo seleccionado es: {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", xpath)
            return t

    def Select_ID_Type(self, id, tipo, dato, tiempo):
        try:
            val = self.SEI(id)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print("El campo seleccionado es: {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", id)
            return t

    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = self.SEX(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", xpath)
            return t

    def Upload_ID(self, id, ruta, tiempo):
        try:
            val = self.SEI(ruta)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", id)
            return t

# funcion radio y check


    def Check_Xpath(self, xpath, tiempo):
        try:
            val = self.SEX(xpath)
            val.click()
            print("Click en el elemento {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", xpath)
            return t

    def Check_ID(self, id, tiempo):
        try:
            val = self.SEI(id)
            val.click()
            print("Click en el elemento {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("El elemento no esta disponible: ", id)
            return t

    def Check_xpath_multiple(self, tiempo, *args):
        try:
            for num in args:
                val = self.SEX(num)
                val.click()
                print("Click en el elemento {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("El elemento no esta disponible: ", num)

    def Existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento", selector)
                return "No existe"
        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento", selector)
                return "No existe"

    def Mouse_Doble(self, tipo, selector, tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t

    def Mouse_Derecho(self, tipo, selector, tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t

    def Mouse_DragAndDrop(self, tipo, selector, destino, tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento {} en {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                val = self.SEI(selector)
                val2 = self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,  val2).perform()
                print("Se solto el elemento {}en {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t

    def Mouse_DragAndDropXY(self, tipo, selector, x, y, tiempo=.2):
        if(tipo=="xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t

    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if(tipo=="xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento {} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t
        elif (tipo=="id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento {} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("El elemento no esta disponible: ", selector)
                return t