import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
t = 2

driver.get("https://demoqa.com/")
driver.maximize_window()

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
# validamos si es visible o esta habilitado
print(titulo.is_displayed())

btn1 = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

if (titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(t)
else:
    print("No existe la imagen")





time.sleep(t)
driver.close()
