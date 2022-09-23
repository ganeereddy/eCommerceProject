import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    #Add customer page
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    txtEmail_name="Email"
    txtPassword_name="Password"
    txtFirstname_id="FirstName"
    txtLastname_id="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDoB_id="DateOfBirth"
    txtCompanyName_id="Company"
    txtCustomerroles_xpath="//div[@class='input-group-append input-group-required']"
    lstitemAdminstrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemGuests_xpath="//li[contains(text(),'Guests')]"
    lstitemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmgrofVendor_xpath="//select[@id='VendorId']"
    txtAddComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txtEmail_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.txtPassword_name).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setDoB(self,dob):
        self.driver.find_element(By.ID,self.txtDoB_id).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID,self.txtCompanyName_id).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.lstitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemAdminstrators_xpath)
        elif role == 'Guests':
            #Here user can be Registered or Guest only
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.lstitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.lstitem.click();
        self.driver.execute_script("arguments[0].click();",self.lstitem)

    def setManageVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAddComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
