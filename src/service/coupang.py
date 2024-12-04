import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.repository.coupang_repository import saveCoupangData


def run():
    coupangData = [
        {
            "category": "카테고리1",
            "products": [
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
        }

    ]

    coupangData.clear()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.coupang.com/np/categories/403245")
    driver.maximize_window()
    sleep(2)

    categoryCodeList = []

    categoryUl = driver.find_element(by=By.CSS_SELECTOR, value="#searchCategoryComponent > ul")
    categoryLis = categoryUl.find_elements(by=By.CSS_SELECTOR, value="& > li")
    for li in categoryLis:
        categoryCodeList.append(li.get_attribute("data-linkcode"))

    driver.close()

    for categoryCode in categoryCodeList[:4]:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"https://www.coupang.com/np/categories/{categoryCode}")
        driver.maximize_window()
        sleep(1)
        category = driver.find_element(by=By.CSS_SELECTOR, value='#searchOptionForm > div > div > div.newcx-main > h1').text
        categoryAndProducts = {
            "category": category,
            "products": []
        }
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
            categoryAndProducts["products"].append(newProduct)
        coupangData.append(categoryAndProducts)
        driver.close()

    saveCoupangData(coupangData)




