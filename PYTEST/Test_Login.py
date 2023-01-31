import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from funciones import Funciones_Globales
from Page_Login import Funciones_Login
t = 2


def test_login1():
    driver = webdriver.Chrome()
    fl = Funciones_Login(driver)
    fl.L1("caita@gmail.com", "1223", "No customer account found")
    fl.L2("", "23432", "Please enter your email")
    fl.L3("cami", "1233", "Wrong email")
    fl.L4("admin@yourstore.com", "admin", "Dashboard")




