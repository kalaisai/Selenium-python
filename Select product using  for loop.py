from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.implicitly_wait(4)
browser.get("https://rahulshettyacademy.com/angularpractice/")

browser.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = browser.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products :
    productName=product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry" :
        product.find_element(By.XPATH, "div/button").click()

browser.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#browser.window_handles.
browser.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
browser.find_element(By.ID, "country").send_keys("India")

wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
browser.find_element(By.LINK_TEXT, "India").click()
browser.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = browser.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText
browser.close()


