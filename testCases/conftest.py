from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
import configparser

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):         #This will get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                 #This will return the browser value to setup method
    return request.config.getoption("browser")

################### PYTEST HTML REPORT #######################

#It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata = {
        "Tester": "Gowtham",
        "Project Name": "NOPCOMMERCE",
    }


# It is hook for Delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

