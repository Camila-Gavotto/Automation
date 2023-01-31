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
t = 1

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

nom = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]")
nom.send_keys("Camila")
nom.send_keys(Keys.TAB + "Gavotto" + Keys.TAB + "cami@gmail.com" + Keys.TAB + "(351)333-2121)" + Keys.TAB + "Direccion 1"
              + Keys.TAB + "Córdoba")
# time.sleep(t)
btn = driver.find_element(By.XPATH, "//input[contains(@name,'phone')]")
ir = driver.execute_script("arguments[0].scrollIntoView();", btn)
# time.sleep(t)
stateSelect = driver.find_element(By.XPATH, "//select[contains(@name,'state')]")
ss = Select(stateSelect)
ss.select_by_visible_text("Oklahoma")
# time.sleep(t)
zip = driver.find_element(By.XPATH, "//input[contains(@name,'zip')]")
zip.send_keys("5050" + Keys.TAB + "www.camilita.com")
# time.sleep(t)
yes = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'yes')]")))
yes.click()
# time.sleep(t)
Pd = driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]")
Pd.send_keys("Feliz automatizando " + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.close()