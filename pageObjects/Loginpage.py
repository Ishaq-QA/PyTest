class Login:
    textbox_userEmail = ("css selector", "[type='text']")
    textbox_userPassword = ("css selector", "[type='password']")

    def __int__(self, driver):
        self.driver = driver

    def setuserEmail(self, username):
        self.driver.find_element("css selector", self.textbox_userEmail).send_keys(username)

    def setuserPassword(self, password):
        self.driver.find_element("css selector", self.textbox_userPassword).send_keys(password)
