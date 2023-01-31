import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

t = .5

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
time.sleep(t)

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://Users//HP//PycharmProjects//Curso_selenium1//Imagenes//demo1.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)

# 1. validamos por try-catch si el elemento existe
# 2. si existe, seleccionalo
# 3. una vez seleccionado, escribe sobre el, la ruta donde esta la imagen y cargala (doble diagonal invertida)
# 4. busco el siguiente elemento + click
# 5. busco el siguiente elemento + click

#Si el elemento no existe, no ejecuta nada de lo del try y manda mensjae "el elemento no existe"
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


time.sleep(t)
driver.close()