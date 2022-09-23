import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import Readconfig
from utilities.customLogeer import LogGen
import string
import random


class Test_003_Addcustomer:
    baseURL= Readconfig.getApplicationURL()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    logger= LogGen.loggen()       #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("**************** Test003_Addcustomer *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Succesful*******************")

        self.logger.info("**************** Starting Add Customer Test *******************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickAddNew()

        self.logger.info("**************** Providing customer information *******************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Ganee")
        self.addcust.setLastName("Reddy")
        self.addcust.setGender("Male")
        self.addcust.setDoB("9/24/1994")
        self.addcust.setCompanyName("Garmin")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManageVendor("Vendor 1")
        self.addcust.setAdminContent("This is for testing......")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving customer info *******************")

        self.logger.info("*************** Add customer validation started *******************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************** Add customer test passed *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcustomer_scr.png")
            self.logger.info("*************** Add customer test failed *******************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending add customer test *******************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


















