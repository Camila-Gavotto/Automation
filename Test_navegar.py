import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

t = 3

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.selenium.dev/documentation/webdriver/elements/locators/")
time.sleep(t)

driver.get("https://cryptomarca.herokuapp.com/register")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

# driver.forward() - pero al poner mas de 3 segundos se bugea, al igual que back()

driver.execute_script("window.history.go(2)")
time.sleep(t)

driver.close()
