import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# iniciamos nuestra clase
class base_test(unittest.TestCase):

#función inicial
    def setUp(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        t = 2
        warnings.simplefilter('ignore', ResourceWarning)

    def test_1(self):
        driver = self.driver
        driver.get("")
        self.driver.maximize_window()
        time.sleep(2)

# funcion de cierre turn down
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__' :
    unittest.main()
