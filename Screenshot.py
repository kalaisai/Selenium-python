from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe", options=chrome_options)


browser.implicitly_wait(2)
browser.get("https://rahulshettyacademy.com/AutomationPractice/")
browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
browser.get_screenshot_as_file("screenshot.png")
