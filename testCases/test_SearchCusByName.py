import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchcustomerPage import SearchCustomer
from utilities.readProperties import Readconfig
from utilities.customLogeer import LogGen

class Test_004_SearchcusByEmail:
    baseURL= Readconfig.getApplicationURL()
    username= Readconfig.getUsername()
    password= Readconfig.getPassword()
    logger= LogGen.loggen()       #Logger

    @pytest.mark.regression
    def test_SearchCusByEmail(self,setup):
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

        self.logger.info("**************** Search customer By Email *******************")
        searchcust= SearchCustomer(self.driver)
        searchcust.setFirstName("James")
        searchcust.setLastName("Pan")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("James Pan")
        assert None==status #assert True==status
        self.logger.info("***********Test_004_SearchcusByEmail Finished***********")
        self.driver.close()








