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
t = 3

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
time.sleep(t)

# Obteniendo todos los links de la pagina
links = driver.find_elements(By.TAG_NAME, "a")
# Una vez que obtenemos todos los elementos que tengan como tag 'a' vamos a imprimirlo
print("El numero de links que hay en la pagina es: ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)

driver.close()