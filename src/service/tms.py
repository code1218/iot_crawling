from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.repository.tms_repository import findWebtoonByTitle


def run():
    title = input("웹툰 제목을 입력하세요: ")
    foundWebtoon = findWebtoonByTitle(title)
    if not foundWebtoon:
        return

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://koritbs.cafe24.com/teacher/index.php')
    sleep(1)

    usernameInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    passwordInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")


    loginButton = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button")
    driver.execute_script("arguments[0].scrollIntoView(true)", loginButton)
    driver.execute_script("arguments[0].click()", loginButton)
    # loginButton.click()
    sleep(5)