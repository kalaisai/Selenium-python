
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.get("https://the-internet.herokuapp.com/windows")
browser.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpen = browser.window_handles
browser.switch_to.window(windowsOpen[1])
print(browser.find_element(By.TAG_NAME, "h3").text)
browser.close()
browser.switch_to.window(windowsOpen[0])
assert "Opening a new window browser" == browser.find_element(By.TAG_NAME, "h3").text
browser.close()
