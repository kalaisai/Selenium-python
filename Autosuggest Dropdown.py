import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")

browser.get("https://rahulshettyacademy.com/dropdownsPractise/")

browser.maximize_window()

browser.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)

countries = browser.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

assert browser.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

time.sleep(5)