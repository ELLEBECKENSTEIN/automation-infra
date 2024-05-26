import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

import test_cases.conftest


class UiActions:
    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        #explicity wait
        elem.click()


    @staticmethod
    @allure.step('updating text')
    def update_text(elem:WebElement, value:str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover tooltip')
    def mouse_hover_tooltip(elem: WebElement):
       ActionChains(test_cases.conftest.driver).move_to_element(elem).click().perform()


    @staticmethod
    @allure.step('mouse hover two element')
    def mouse_hover(elem1:WebElement,elem2:WebElement):
        test_cases.conftest.ActionChains(test_cases.conftest.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('right click on element')
    def right_click(elem:WebElement):
        test_cases.conftest.ActionChains(test_cases.conftest.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('drag and drop')
    def drag_and_drop(elem1:WebElement,elem2:WebElement):
        test_cases.conftest.ActionChains(test_cases.conftest.driver).drag_and_drop(elem1,elem2).perform()

    @staticmethod
    @allure.step('clear text field in element')
    def clear(elem:WebElement):
        elem.clear()

    @staticmethod
    def select_option_by_text(select_element,option_text):
        dropdown= Select(select_element)
        dropdown.select_by_visible_text(option_text)

    @staticmethod
    def select_option_by_index(select_element,index):
        dropdown= Select(select_element)
        dropdown.select_by_index(index)

    @staticmethod
    def select_option_by_value(select_element,value):
        dropdown= Select(select_element)
        dropdown.select_by_value(value)











