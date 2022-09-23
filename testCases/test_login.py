import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogeer import LogGen

class Test001_Login:
    baseURL= Readconfig.getApplicationURL()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    logger= LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**************** Test001_Login *****************")
        self.logger.info("**************** Verifying Homepage Title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Homepage Title test is Passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")  #when fail need to capture s.shot
            self.driver.close()
            self.logger.error("**************** Homepage Title test is Failed *****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************** Verifying Login test *****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************** Login test Passed *****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("**************** Login test Failed *****************")
            assert False
