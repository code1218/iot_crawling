from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.kyobobook.co.kr')
    sleep(1)

    searchInput = driver.find_element(by=By.CSS_SELECTOR, value='#searchKeyword')
    searchInput.send_keys("파이썬")
    sleep(2)

    searchButton = driver.find_element(By.CSS_SELECTOR, value='#welcome_header_wrap > div.header_inner > div > div.gnb_search_box > a')
    searchButton.click()
    sleep(5)