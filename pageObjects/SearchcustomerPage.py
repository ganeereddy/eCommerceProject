from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    #Add customer page
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    tblSearchresults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tblrows_xpath="//table[@id='customers-grid']//tbody/tr"
    tblcolumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.ID, self.tblrows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.ID, self.tblcolumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag=True
                break
            return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag=True
                break
            return flag








