import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = .7

diaSelect = driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")
ds = Select(diaSelect) # indico que a la variable diaSelect se le agrega la funcion select, para despues utilizarla de las 3 formas de abajo

ds.select_by_visible_text("Sunday")
time.sleep(t)

ds.select_by_index(3)
time.sleep(t)

ds.select_by_value("Saturday")
time.sleep(t)

ciudad = Select(driver.find_element(By.ID, "multi-select"))
time.sleep(t)

ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(3)
time.sleep(t)
ciudad.select_by_index(6)
time.sleep(t)


driver.close()