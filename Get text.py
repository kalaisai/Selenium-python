
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
browser.implicitly_wait(2)
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")

browser.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)

results = browser.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

browser.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
browser.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#SUM VALIDATION
prices = browser.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0

for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount=int(browser.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

browser.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
browser.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

print(browser.find_element(By.CLASS_NAME, "promoInfo").text)

discountAmount = float(browser.find_element(By.CLASS_NAME, ".discountAmt").text)

print(discountAmount)

assert totalAmount > discountAmount

browser.close()
