import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")
nom.send_keys("Camila")
nom.send_keys(Keys.TAB + "cami@gmail.com" + Keys.TAB + "Direccion uno" + Keys.TAB + "Direccion dos " + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(4)

driver.find_element(By.XPATH, "(//span[@class='text'])[2]").click()
time.sleep(2)

driver.close()