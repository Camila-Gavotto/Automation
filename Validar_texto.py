import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
t = 2

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(t)

name_val = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
name = name_val.text
# print("El valor del error es: ", name)

if (name == "Please supply your first name"):
    cn = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]")
    cn.send_keys("Camila")
    time.sleep(t)
    print("Nombre correcto")
else:
    print("Falta el nombre")

ap_val = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")
ap = ap_val.text
# print("El valor del error es: ", name)

if (ap == "Please supply your last name"):
    ap = driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]")
    ap.send_keys("Gavotto")
    time.sleep(t)
    print("Apellido correcto")
else:
    print("Falta el apellido")

print(btn.is_enabled())
if (btn.is_enabled()==False):
    print("Faltan campos por llenar")
else:
    print("Listo todo ok")

time.sleep(t)
driver.close()