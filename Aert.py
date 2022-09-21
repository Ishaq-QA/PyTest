from selenium import webdriver
import time

from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element("xpath", "//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
alert = driver.switch_to_alert()
alert.accept()
#  This method dismisses an alert pop up.
# alert.dismiss()
# This method switches focus to alert.
# driver.switch_to.alert
# This method extracts text from the alert pop up.
# print(alert.text)



