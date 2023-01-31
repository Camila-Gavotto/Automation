import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
nom.send_keys("Camila")
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("cami@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("Direccion uno")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion dos")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
time.sleep(2)

driver.close()
