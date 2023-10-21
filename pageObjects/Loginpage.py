from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    textbox_Email_name = "Email"
    textbox_Password_id = "Password"
    button_Login_xpath = "//button[text()='Log in']"
    link_Logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.textbox_Email_name).clear()
        self.driver.find_element(By.NAME,self.textbox_Email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_Password_id).clear()
        self.driver.find_element(By.ID,self.textbox_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_Logout_xpath).click()






