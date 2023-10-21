import time

from selenium import webdriver
import pytest
from pageObjects.Loginpage import Login
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()               # Logger Code

    def test_homepageTitle(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Home Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********************** HomePage is passed *************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Screenshot1.png")
            self.driver.close()
            self.logger.info("*********************** HomePage is Failed *************************************")
            assert False



    def test_login(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Admin Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********************** Login DashBoardPage is passed *************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Screenshot2.png")
            self.driver.close()
            self.logger.info("*********************** Login DashBoardPage is failed *************************************")
            assert False


