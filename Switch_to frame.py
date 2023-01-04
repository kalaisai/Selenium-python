from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.implicitly_wait(2)
browser.get("https://the-internet.herokuapp.com/iframe")
browser.switch_to.frame("mce_0_ifr")
browser.find_element(By.ID, "tinymce").clear()
browser.find_element(By.ID, "tinymce").send_keys("I am getting error")
browser.switch_to.default_content()
print(browser.find_element(By.CSS_SELECTOR, "h3").text)
browser.quit()

