
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certification-errors")



browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe",options=chrome_options)

browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")

print(browser.title)
