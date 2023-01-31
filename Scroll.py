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

t = 3

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)

# driver.execute_script("window.scrollTo(0,1000)")

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    Buscar = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    # con esta función estamos diciendo vete a donde este el elemento
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


time.sleep(t)
driver.close()