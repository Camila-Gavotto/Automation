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

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)

try:
    # 1 detecta el elemento
    # 2 cuando lo detecta hace click y lo cierra
    # Esto es un explicity wait, que el elemento este clickeable para darle click
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    Buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(t)

    # si no lo encuentra que me mande este mensaje
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible")


time.sleep(t)
driver.close()
