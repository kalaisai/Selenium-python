import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
browser.implicitly_wait(5)
browser.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(browser)
#action.double_click()
#action.drag_and_drop()
action.move_to_element(browser.find_element(By.ID, "mousehover")).perform()
action.context_click(browser.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(browser.find_element(By.LINK_TEXT, "Reload")).click().perform()




