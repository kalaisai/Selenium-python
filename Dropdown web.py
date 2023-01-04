import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")

browser.get("https://rahulshettyacademy.com/angularpractice/")

browser.maximize_window()

browser.find_element(By.ID, "autosuggest").send_keys("India")

country = browser.find_elements(By.CSS_SELECTOR, "#autosuggest")
print(len(country))

dropdown = Select(browser.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

time.sleep(5)
