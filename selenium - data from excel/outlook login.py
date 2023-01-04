import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

# Login
browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
browser.get("https://outlook.live.com/owa/")
browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//a[@class='internal sign-in-link' and text()='Sign in']").click()
browser.find_element(By.XPATH, "//input[@type='email']").send_keys("")
browser.find_element(By.ID, "idSIButton9").click()
password_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "passwd")))
password_button.send_keys("")
browser.find_element(By.XPATH, "//input[@type='submit']").click()
browser.find_element(By.ID, "idSIButton9").click()
time.sleep(10)







