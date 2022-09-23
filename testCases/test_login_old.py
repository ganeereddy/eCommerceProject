from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")  #when fail need to capture s.shot
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
