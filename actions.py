import time


import slider
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import window

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


service_obj = Service(".\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)


### DRAG AND DROP & DRAG AND DROP OFFSET

driver.get("https://jqueryui.com/droppable/")
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
ele1 = driver.find_element(By.ID, "draggable")
ele2 = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop_by_offset(ele1, 80,65).perform()
time.sleep(4)


### KEYBOARD ELEMENT COPY PASTE

driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
a = ActionChains(driver)
NME = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("Kalai")
EML = driver.find_element(By.XPATH, "//input[@name='email']")
a.key_down(Keys.CONTROL).send_keys("a").perform()
a.key_down(Keys.CONTROL).send_keys("c").perform()
a.click_and_hold(EML).perform()
a.key_down(Keys.CONTROL).send_keys("v").perform()
time.sleep(2)
a.key_down(Keys.BACK_SPACE).perform()
time.sleep(4)

### CLICK AND HOLD & RELEASE

driver.get("https://selenium08.blogspot.com/2020/01/click-and-hold.html")
time.sleep(2)
BtnA = driver.find_element(By.XPATH, "//li[@name='A']")
BtnF = driver.find_element(By.XPATH, "//li[@name='F']")
actions = ActionChains(driver)
actions.move_to_element(BtnA)
actions.click_and_hold()
actions.move_to_element(BtnF).perform()
actions.release().perform()
time.sleep(3)
### DOUBLE CLICK
actions.double_click(BtnF)
actions.perform()
time.sleep(3)

# driver.get("https://sqa.stackexchange.com/questions/15527/handling-the-unexpected-popup-ads-in-website")
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[normalize-space()='Accept all cookies']").click()
# time.sleep(2)

### SCROLL DOWN AND UP - VERTICAL

driver.get("https://selenium08.blogspot.com/2020/02/vertical-scroll.html")
time.sleep(2)
actions = ActionChains(driver)
actions.scroll_by_amount(2,99).perform()
targetEle = driver.find_element(By.XPATH, "//a[normalize-space()='Science']")
actions.scroll_to_element(targetEle).perform()
actions.scroll_by_amount(2,-99).perform()
time.sleep(5)

#### SCROLL-HORIZONTAL

driver.get("https://selenium08.blogspot.com/2020/02/horizontal-scroll.html")
time.sleep(2)
actions = ActionChains(driver)
actions.scroll_by_amount(2, 400).perform()
iframe = driver.switch_to.active_element.find_element(By.XPATH, "//div[@class='scrollmenu']")
iframe2 = driver.find_element(By.XPATH, "//a[normalize-space()='Technology']")
actions.scroll_to_element(iframe2).perform()
time.sleep(3)


#### alert
driver.get("https://www.tnpsc.gov.in/")
time.sleep(2)
driver.find_element(By.XPATH, "//h3[normalize-space()='Registered User']").click()
time.sleep(3)
my_alert = driver.switch_to.alert
my_alert.accept()
time.sleep(4)








