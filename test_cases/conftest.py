import os
import time

import allure
import mysql.connector
import pytest
import selenium.webdriver
import appium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import Manage_Pages

driver= None
action=None
action2= None
m_action= None
mobile_size= None
web_driver= 'Chrome'
db_connector = None
eyes= Eyes() #applitools

@pytest.fixture(scope='class')
def init_web_driver(request):
    if get_data('Execute_Applitools').lower() == 'yes':
        globals()['driver'] = get_web_driver()
    else:
        edriver= get_web_driver()
        globals()['driver']= edriver
    driver=globals()['driver']
    # driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver=driver
    Manage_Pages.init_web_pages()
    globals()['action']= ActionChains(driver)
    Manage_Pages.init_web_pages()

    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.api.key= get_data('Applitools_Key')
    yield
    driver.quit()
    if get_data('Execute_Applitools').lower() == 'yes':
        eyes.close() #applitools
        eyes.abort() #applitools

@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = edriver
    driver=globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action']= TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2']= TouchAction(driver)
    request.cls.action = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['m_action']
    Manage_Pages.init_mobile_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver , EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    Manage_Pages.init_electron_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    Manage_Pages.init_dasktop_pages()
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_db_connection(request):
    db_connector = mysql.connector.connect(
        host=get_data('DB_Host'),
        database=get_data('DB_Name'),
        user=get_data('DB_User'),
        password=get_data('DB_Password')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()






def get_web_driver():
    web_driver = get_data('Browser')
    # web_driver = os.getenv('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver=None
        raise Exception('wrong input, Unrecognized Browzer')
    return driver


def get_mobile_driver():
    if get_data('Mobile_Device').lower() == 'android':
        driver= get_android(get_data('Udid'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver= get_ios(get_data('Udid'))
    else:
        driver=None
        raise Exception('Wrong input, unrecognized mobile OS')
    return driver


def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('Electron_App')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('Electron_Driver'))
    return driver

def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('Application_Name')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriver_Service'), dc)
    return driver





def get_chrome():
    # srv= Service(ChromeDriverManager().install()) #seleniuom 4.x
    # chrome_driver=selenium.webdriver.Chrome(service=srv)             #selenium 4.x
    chrome_driver= selenium.webdriver.Chrome(ChromeDriverManager().install())  #selenium 3.x
    return chrome_driver


def get_firefox():
    # srv= Service(executable_path=GeckoDriverManager().install()) #seleniuom 4.x
    # ff_driver= selenium.webdriver.Firefox(service=srv) #selenium 4.x
    ff_driver= selenium.webdriver.Firefox(GeckoDriverManager().install()) #selenium 3.x
    return ff_driver


def get_edge():
    # srv= Service(EdgeChromiumDriverManager().install()) #seleniuom 4.x
    # edge_driver= selenium.webdriver.Edge(service=srv) #selenium 4.x
    edge_driver= selenium.webdriver.Edge(EdgeChromiumDriverManager().install()) #selenium 3.x
    return edge_driver


def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('Appium_Server'),dc)
    return android_driver

def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_Id')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return ios_driver



#catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None: #if it is None -> this is exeption from API test
             image= get_data('ScreenShotPath') + 'screen_' + str(get_time_stamp()) + '.png'
             globals()['driver'].get_screenshot_as_file(image)
             allure.attach.file(image, attachment_type=allure.attachment_type.PNG)








