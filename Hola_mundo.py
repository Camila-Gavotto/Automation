from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.webdriver import Service

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")
print(driver.title)

driver.close()
