import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(15)
# implicity wait - le da tiempo al navegador para localizar los objetos, tienes hasta 15s para esperar un objeto
# si el navegador encuentra el objeto, lo va a poner , no va a esperar los 15s, y va a acabar la prueba
# los 15s son si no lo encuentra, se toma 15s buscandolo, si no encuentra, arroja el error, despues de los 15s

t = .1
time.sleep(t)

nom = driver.find_element(By.CSS_SELECTOR, '#userName')
nom.send_keys("Camila")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("cami@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("Direccion uno")
time.sleep(t)
driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion dos")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

driver.find_element(By.XPATH, "//button[contains(@id,'submit')]").click()
time.sleep(t)

driver.close()