import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd


dataframe = pd.read_excel('Outlook.xlsx')

#Login
browser = webdriver.Chrome(".\\chromedriver_win32\\chromedriver.exe")
browser.maximize_window()
browser.get("https://outlook.live.com/owa/")
browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//a[@class='internal sign-in-link' and text()='Sign in']").click()
browser.find_element(By.XPATH, "//input[@type='email']").send_keys("")
browser.find_element(By.ID, "idSIButton9").click()
password_button = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "passwd")))
password_button.send_keys("")
browser.find_element(By.XPATH, "//input[@type='submit']").click()
browser.find_element(By.ID, "idSIButton9").click()
time.sleep(2)
for index, i in enumerate( dataframe.index):
    print(dataframe.loc[i], end='\n\n')
    browser.find_element(By.XPATH, "//button[@aria-label='New mail']//span[@class='flexContainer-160']").click()
    browser.find_element(By.XPATH, "//div[@aria-label='To']").send_keys(dataframe.loc[i]['Emails'])
    Anush = browser.find_element(By.XPATH, "//span[@class='MwdHX']")
    actions = ActionChains(browser)
    actions.move_to_element(Anush).click().perform()
    Subj = browser.find_element(By.XPATH, "//div[@class='P6mmz']")
    actions.click(Subj).send_keys("Reg:Testing").perform()
    Message = browser.find_element(By.XPATH, "(//div[@class='elementToProof'])[1]")
    Message_content = """
    Hii this is Kalai..
    sending some emails for testing...
    Is that any emails received....  """
    actions.click(Message).send_keys(Message_content).perform()
    browser.find_element(By.XPATH, "//button[@title='Send (Ctrl+Enter)']").click()

    time.sleep(3)
    #browser.find_element(By.XPATH, "//button[@id='ok-1']").click()

