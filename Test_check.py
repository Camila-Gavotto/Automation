import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://www.musimundo.com/telefonia/telefonos-celulares/c/82")
driver.maximize_window()
driver.implicitly_wait(10)

t = 2

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'block-link')])[1]")))
btn1.click()

btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'block-link')])[3]")))
btn3.click()

btn5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'block-link')])[5]")))
btn5.click()

time.sleep(t)
driver.close()
