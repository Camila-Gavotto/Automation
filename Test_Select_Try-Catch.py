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

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = 2

# Si encuentra el elemento (con la primer línea), ejecutame lo de abajo
try:
    diaSelect = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'select-demo')]")))
    dias = Select(diaSelect)

    dias.select_by_visible_text("Sunday")
    time.sleep(t)
    dias.select_by_index(2)
    time.sleep(t)
    dias.select_by_value("Thursday")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

ciudad = Select(driver.find_element(By.ID, "multi-select"))
time.sleep(t)

ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(3)
time.sleep(t)
ciudad.select_by_index(6)
time.sleep(t)


driver.close()