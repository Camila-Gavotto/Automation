import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# option agrega mas variantes al browser, le podes indicar que te lo abra en una ventana de incognito o sin extensiones por ejemplo
# options = webdriver.ChromeOptions()
# options.add_experimental_option()
driver = webdriver.Chrome() #  (options=options)
# aca le estamos diciendo construime el chrome para simular chrome y el webdriver (que construye el chrome) esta ubicado en esa ruta
driver.get("https://anses.gob.ar/")
time.sleep(2)
# esta linea es una peticion request de metodo get, que es para decirle a que pagina vamos a acceder
search = driver.find_element(By.ID, "edit-search-api-fulltext")
# ahora necesitamos decirle a selenium que es lo que necesitamos clickear, guardar, escribir, etc
# le decimos que busque ese elemento por su ID, y una vez que lo encuentr elo guarde en la variable search
search.send_keys("Refuerzo alimentario" + Keys.ENTER)
# ahora vamos a decirle que necesitamos hacer con ese elemento, la forma que tiene selenium es con send keys
time.sleep(2)


time.sleep(2)
link.click()
time.sleep(2)

# se recomienda cerrar la automatizacion
driver.close()