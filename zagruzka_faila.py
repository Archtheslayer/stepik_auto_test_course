from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)')
    input2.send_keys('Ivanov')

    input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)')
    input2.send_keys('test@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()