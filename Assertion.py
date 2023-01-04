import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browserSortedVeggies = []
browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")

browser.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on the column button

#browser.find_element(By.CSS_SELECTOR, "#root > div > header > div > div.cart > a:nth-child(2)").click()
browser.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all  vegggies names
veggieWebElement = browser.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElement:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#sort this veggies --> new sorted list
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
time.sleep(5)
browser.quit()