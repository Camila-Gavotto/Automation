import time  #la automatizacion la hace tan rapido, que para poder ver si va ok, le ponemos un pequeño delay . esta la trae python, no selenium. Selenium tiene modulo WAIT
from selenium import webdriver  # este impor es para simular o montar el browser, sin esto no podria creer o simular la pantalla donde voy a automatizar
from selenium.webdriver.common.by import By  # este te permite buscar elementos en la pagina, sin esto no podrias buscar por nombre clase nada
from selenium.webdriver.common.keys import Keys  # este es para hacer un input, para poder agregar un texto por ejemplo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# le decimos que browser vamos a simular 
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
t = 1
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Camila" + Keys.TAB + "Gavotto" + Keys.TAB + "cami@gmail.com")
driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("(351)333-2121)" + Keys.TAB + "Direccion 1" + Keys.TAB + "Córdoba")
stateSelect = Select(driver.find_element(By.XPATH, "//select[contains(@name,'state')]"))
stateSelect.select_by_index(5)
driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("5050" + Keys.TAB + "www.camilita.com")
driver.find_element(By.XPATH, "//input[contains(@value,'yes')]").click()
driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("Feliz automatizando " + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.close()