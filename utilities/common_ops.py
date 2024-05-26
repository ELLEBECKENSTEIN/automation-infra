import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_cases.conftest
import xml.etree.ElementTree as ET


############################################################################
# Function Name: get_data
# Function Description : This function reads data from external xml file
#Function Parameters: String - node(tag) name
#Function Return: String - node (tag) value
##########################################################################
def get_data(node_name):
    root=ET.parse('C:/Automation/pythonProject/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

def wait(for_element,elem):
    if for_element=='element_exists':
        WebDriverWait(test_cases.conftest.driver, int(get_data('WaitTime'))).until(expected_conditions.presence_of_element_located((elem[0],elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(test_cases.conftest.driver, int(get_data('WaitTime'))).until(expected_conditions.visibility_of_element_located((elem[0],elem[1])))

def read_csv(file_name):
    data= []
    with open(file_name, newline='') as file:
        reader= csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data

def get_time_stamp():
    return time.time()


#enum for selecting displayed element or exist element, my wait method used this enum
class For:
    ELEMENT_EXISTS= 'element_exists'
    ELEMENT_DISPLAYED='element_displayed'

#enum for selecting row from table to delete
class By:
    User= 'user'
    Index= 'index'

#enum for selecting whether we want to save mortgage transaction or not
class Save:
    Yes = True
    No = False


#enum for selecting whether we want to save mortgage transaction or not
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN= 'down'






