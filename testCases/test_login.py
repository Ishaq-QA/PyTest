import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Loginpage import Login


class LoginTest_01:
    baseURL = "https://app-traxidy.thedemo.co/"
    username = "aram.zahedi@247labs.com"
    password = "123456"

    def Login_page_title(self):
        self.driver.get(self.baseURL)
        Title = self.driver.title
        if Title == "Traxidy WebApp - Traxidy WebApp":
            assert True
        else:
            assert False

    def LoginPage_test(self):
        driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.LP = Login()
        self.LP.setUserName(self.username)
        self.LP.setUserPassword(self.password)
