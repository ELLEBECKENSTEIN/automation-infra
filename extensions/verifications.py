import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert actual==expected,'Verify Equals Failed, Actual:'+str(actual) + 'is not Equals to Expected: ' +str(expected)


    @staticmethod
    @allure.step('verify element is displayed')
    def is_displayed(elem:WebElement):
        assert elem.is_displayed(),'Verify is displayed Failed, Element: ' + elem.text + 'is not Displayed'



    #Verify Menu Buttons Using Smart-assertions
    @staticmethod
    @allure.step('soft verifications (assert) of elements using smart-assertions')
    def soft_assert(elems):
        for i in range(len(elems)):
             soft_assert(elems[i].is_displayed(), "elem is not displayed")
        verify_expectations()


    # Verify Menu Buttons Using My Implementation
    @staticmethod
    @allure.step('soft verifications (assert) of elements using my implementation')
    def soft_displayed(elems):
        failed_elems=[]
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria_label'))
        if len(failed_elems)>0 :
            for failed_elem in failed_elems:
                print('soft Displayed Failed, Elements which have failed: ' + str(failed_elem))
            raise AssertionError('soft Displayed Failed')


    @staticmethod
    @allure.step('verify number of elements in list')
    def verify_number_of_elements(elems, size):
        assert len(elems)== size, 'Number of elements in list: ' + str(len(elems)) + ' does not match expected:' + str(size)
