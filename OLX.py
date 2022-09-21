from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('http://olx.com.pk/')
search = browser.find_element("xpath",
                              "//*[@id='body-wrapper']/div/header/div[2]/div[3]/div/div/div[1]/div/div[1]/input")
search.send_keys("Iphone")
search_button = browser.find_element("xpath", "//*[@id='body-wrapper']/div/header/div[2]/div[3]/div/div/div[1]/button")
search_button.click()
browser.implicitly_wait(30)
# Some time wait ka masla occurs
# time.sleep(1)

list_items = []
items_list = []
items_innerHTML = []
items_lower = []

list_items = browser.find_elements("css selector", '[aria-label="Listing"]')
for items in list_items:
    items_list += items.find_elements(
        "css selector", '[aria-label="Title"]')
for item in items_list:
    items_innerHTML.append(item.get_attribute('innerHTML'))
print("List Of Iphones = ", items_innerHTML)
ran = len(items_innerHTML)
assert_list = []
for i in range(ran):
    if "iphone" or "Iphone" or "IPHONE" or "IPhone" or "iPhone" in items_innerHTML[i]:
        assert_list.append("true")
    else:
        assert_list.append("false")
    assert "true" in assert_list
browser.close()
