import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
browser.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "kalai"
browser.find_element(By.ID, "checkBoxOption2").click()

radiobutton = browser.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobutton[2].click()

assert radiobutton[2].is_selected()
browser.find_element(By.ID, "hide-textbox").click()

assert not browser.find_element(By.ID, "displayed-text").is_displayed()
browser.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
browser.find_element(By.ID, "alertbtn").click()
alert=browser.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

