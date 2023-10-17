from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
list1 = []
list2 = []
try:
    driver.get(url='https://www.adidas.com/us/men-tops')
    for i in range(1, 10):
        shirt_name = driver.find_element(By.CSS_SELECTOR, f'#main-content > div > div:nth-child(3) > div > div > div.col-s-12.col-l-17.col-xl-18.no-x-padding-on-mobile___3dhA9 > div.product-container___3GvlZ > div > div:nth-child({i}) > div > div > div > div > div > div > a > div > p.glass-product-card__title')
        shirt_price = driver.find_element(By.CSS_SELECTOR, f'#main-content > div > div:nth-child(3) > div > div > div.col-s-12.col-l-17.col-xl-18.no-x-padding-on-mobile___3dhA9 > div.product-container___3GvlZ > div > div:nth-child({i}) > div > div > div > div > div > div > div.glass-product-card__assets > a.product-card-content-badges-wrapper___2RWqS > div > div > div')
        shirt_price = shirt_price.text
        shirt_price = shirt_price.split('\n')[0]
        list1.append(shirt_name.text)
        list2.append(shirt_price)
    df = pd.DataFrame(data=list1, columns=['shirt'])
    df['price'] = list2
    df.to_csv('data.csv', index=False, index_label=False)
except Exception as ex:
    print(ex.__class__.__name__)
finally:
    driver.close()
    driver.quit()

    