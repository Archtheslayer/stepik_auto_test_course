from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://vk.com"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    btn1 = browser.find_element(By.XPATH, '//*[@id="index_login"]/div/form/button[1]/span/span')
    btn1.click()

    input1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/section/div/div/div/input')
    input1.send_keys('login')

    btn2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/button/div')
    btn2.click()

    parol = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/div[2]/div[1]/div/input')
    parol.send_keys('password')

    btn3 = browser.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/button/div')
    btn3.click()

    btn4 = browser.find_element(By.XPATH, '//*[@id="l_msg"]/a/span[1]')
    btn4.click()

    btn5 = browser.find_element(By.XPATH, '//*[@id="im_dialogs"]/div[1]/div[1]/div/div[1]/li[3]/div[2]/div')
    btn5.click()

    msg = browser.find_element(By.XPATH, '//*[@id="im_editable0"]')
    msg.send_keys('Привет! Это сообщение я написал тебе благодарю написанному мною скрипту с помощью Python и Selenium!')

    sent_msg = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button/span[2]')
    sent_msg.click()



finally:
    time.sleep(5)
    browser.quit()