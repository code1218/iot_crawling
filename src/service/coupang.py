import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run():
    coupangData = [
        {
            "productName": "상품1",
            "price": 10000,
            "productImgUrl": "https://~~~~~"
        },
        {
            "productName": "상품2",
            "price": 20000,
            "productImgUrl": "https://~~~~~"
        }
    ]

    coupangData.clear()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.coupang.com/np/categories/403245")
    driver.maximize_window()
    sleep(2)

    category = driver.find_element(by=By.CSS_SELECTOR, value='#searchOptionForm > div > div > div.newcx-main > h1').text
    print(category)

    ul = driver.find_element(by=By.CSS_SELECTOR, value="#productList")
    dlList = ul.find_elements(by=By.CSS_SELECTOR, value="li > a > dl")
    for dl in dlList:
        driver.execute_script("arguments[0].scrollIntoView()", dl)
        productName = dl.find_element(by=By.CSS_SELECTOR, value="dd > div:nth-of-type(2)").text
        price = dl.find_element(by=By.CSS_SELECTOR, value="dd > div:nth-of-type(3) .price-value").text
        productImgUrl = dl.find_element(by=By.CSS_SELECTOR, value="dt > img").get_attribute("src")
        newProduct = {
            "productName": productName,
            "price": price,
            "productImgUrl": productImgUrl
        }
        coupangData.append(newProduct)

        print(f"""
상품명: {productName}
가격: {price}
상품이미지: {productImgUrl}
""")


