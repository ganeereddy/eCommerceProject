from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
        print("Launching chrome browser......")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=r"C:\Drivers\geckodriver_win64\geckodriver.exe")
        print("Launching chrome browser......")
    else:
        driver = webdriver.Edge("C:\Drivers\edgedriver_win64\msedgedriver.exe")
    return driver

def pytest_addoption(parser):     # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # This will return the Browser value to setup method
    return request.config.getoption("--browser")

#### Pytest HTML Report ##########

#It is hook for adding Environment info to the HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Ganee'

#It is hook for delete/modify Environment info into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)












