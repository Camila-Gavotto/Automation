import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://www.carrefour.it/")
driver.maximize_window()
# driver.implicitly_wait(10)
t = 2

btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
btn.click()
"""
TAMBIEN PUEDE IR ESTO - VISITAR LA PAGINA PARA VER EL RESTO..
btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
btn.click()
"""
time.sleep(t)

driver.find_element(By.XPATH, "//input[contains(@class,'input-bar')]").send_keys("Bienvenido a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.find_element(By.XPATH, "//a[@class='btn btn-primary'][contains(.,'Vai a Spesa Online')]").send_keys(Keys.ENTER)


time.sleep(t)
driver.close()
