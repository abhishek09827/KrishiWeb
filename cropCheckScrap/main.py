import os
import time

from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('https://www.justdial.com/Bangalore/Soil-Testing-Laboratory-near-me')
up_location = driver.find_element(By.CSS_SELECTOR, 'button[class*="inputgroup_alert_button"]')
up_location.click()
det_location = driver.find_element(By.CSS_SELECTOR, 'div[class*="input_location_detect"]')
det_location.click()
sort = driver.find_element(By.CSS_SELECTOR, 'div[class*="jsx-6ab5af3a8693e5db"]')
sort.click()

search_res_1 = driver.find_element(By.CSS_SELECTOR, 'div[class*="resultbox_listview"]')
search_res_2 = search_res_1.find_elements(By.CLASS_NAME,
        'resultbox_info'
    )


collection = []
for i in search_res_2:

    name = i.find_element(By.CSS_SELECTOR,
        'a[class*="resultbox_title"]'
    ).get_attribute('title').strip()

    address = i.find_element(By.CSS_SELECTOR,
        'div[class*="font15"]'
    ).get_attribute('innerHTML').strip()
    img = i.find_element(By.CSS_SELECTOR,
                             'img[class*="resultbox_image"]'
                             ).get_attribute('src').strip()

    link = i.find_element(By.CSS_SELECTOR,
        'a[class*="resultbox_title_anchor"]'
    ).get_attribute('href').split()



    collection.append(
            [name, address,img, link]
        )

table = PrettyTable(
            field_names=["name", "address", "img","link"]
        )
table.add_rows(collection)
print(table)

driver.implicitly_wait(30)
time.sleep(50)