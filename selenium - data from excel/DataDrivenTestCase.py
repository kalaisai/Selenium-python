import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import Utilities
from Utilities import XLutility

browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
path = "C:\\Users\\KalaimathiSaiKannan\\Documents\\Excel.xlsx"
rows = XLutility.getRowCount(path, 'Sheet1')
browser.get("https://outlook.live.com/owa/")
browser.maximize_window()
browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//a[@class='internal sign-in-link' and text()='Sign in']").click()

for r in range(2, rows + 1):

    Emails = XLutility.readData(path, "Sheet1", r, 1)
    Password = XLutility.readData(path, "Sheet1", r, 2)
    browser.find_element(By.XPATH, "//input[@type='email']").send_keys(Emails)
    browser.find_element(By.ID, "idSIButton9").click()
    XLutility.writeData(path, 'Sheet1', r, 3, "Email passed")
    try:
        browser.find_element(By.ID, "usernameError").is_displayed()
        alert = browser.find_element(By.ID, "usernameError").text
        print(alert)
        XLutility.writeData(path, 'Sheet1', r, 3, "Email failed")
        break
    except Exception:
        browser.implicitly_wait(2)
        password_button = WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "passwd")))
        password_button.send_keys(Password)
        browser.find_element(By.XPATH, "//input[@type='submit']").click()
        try:
            #browser.find_element(By.XPATH, "//input[@type='checkbox']").click()
            browser.find_element(By.ID, "idSIButton9").click()
            XLutility.writeData(path, 'Sheet1', r, 4, "Password passed")
        except Exception:
            XLutility.writeData(path, 'Sheet1', r, 4, "Password passed")

        try:
            browser.implicitly_wait(10)

            ##menu list
            wait = WebDriverWait(browser, 10)
            menu = browser.find_element(By.XPATH, "//div[@class='DPg26']").text
            print(menu)

            ##inbox
            inbox = browser.find_element(By.XPATH, "//span[@class='gtcPn u0T8k LPIso wk4Sg']").click()
            browser.find_element(By.XPATH, "(//div[@class='XG5Jd JtO0E'])[1]").click()
            browser.find_element(By.XPATH, "//div[@class='Xk9aW Z9nT9']").click()
            browser.find_element(By.XPATH, "//button[@name='Unread']").click()
            time.sleep(2)

            ##search
            browser.find_element(By.XPATH, "//input[@id='topSearchInput']").send_keys("Muthu")
            wait1 = WebDriverWait(browser, 5)
            MouseHower = browser.find_element(By.XPATH, "//div[@id='searchSuggestion-0']")
            actions = ActionChains(browser)
            actions.move_to_element(MouseHower).click().perform()

            ##delete
            browser.find_element(By.XPATH, "//div[@class='DPg26']//div[@title='Deleted Items']").click()
            browser.find_element(By.XPATH, "(//div[@aria-label='Select a conversation'])[1]").click()
            browser.find_element(By.XPATH, "//button[@aria-label='Delete']").click()
            browser.find_element(By.XPATH, "//button[@id='ok-1']").click()

            ##signin
            browser.find_element(By.XPATH, "//div[@class='_2r3tGOSyvyUola8y7ahgJG undefined']").click()
            browser.find_element(By.ID, "mectrl_signInItem").click()
            browser.find_element(By.ID, "otherTileText").click()
            time.sleep(4)


        except Exception:
            XLutility.writeData(path, 'Sheet1', r, 4, "Password failed")


