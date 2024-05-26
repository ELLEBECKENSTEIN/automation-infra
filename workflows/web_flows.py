import allure

import page_objects.web_objects.main_page
import page_objects.web_objects.server_admin_page
import page_objects
import utilities.manage_pages
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from page_objects.web_objects import main_page
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:
    @staticmethod
    @allure.step('login to grafana flow')
    def login_flow(user:str ,password:str ):
        UiActions.update_text(utilities.manage_pages.web_login.get_user_name(), user)
        UiActions.update_text(utilities.manage_pages.web_login.get_password(), password)
        UiActions.click(utilities.manage_pages.web_login.get_submit())
        UiActions.click(utilities.manage_pages.web_login.get_skip())

    @staticmethod
    @allure.step('verify grafana title flow')
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXISTS, main_page.main_title)
        actual=utilities.manage_pages.web_main.get_main_title().text
        Verifications.verify_equals(actual,expected)


    # Verify Menu Buttons Using My Implementation
    @staticmethod
    @allure.step('verify displayed menu button flow using my implementation')
    def verify_menu_buttons_flow():
        elems=[utilities.manage_pages.web_upper_menu.get_panel(),
               utilities.manage_pages.web_upper_menu.get_save_dashboard(),
               utilities.manage_pages.web_upper_menu.get_dashboard_settings(),
               utilities.manage_pages.web_upper_menu.get_cycle_view()]
        Verifications.soft_displayed(elems)

    @staticmethod
    @allure.step('go to users flow')
    def open_users():
        elem1= utilities.manage_pages.web_left_menu.get_server_admin()
        elem2=utilities.manage_pages.web_server_admin_menu.get_users()
        UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    @allure.step('create new user flow')
    def create_user(name, email, user, password):
        UiActions.click(utilities.manage_pages.web_server_admin.get_new_user())
        UiActions.update_text(utilities.manage_pages.web_server_admin_new_user.get_name(), name)
        UiActions.update_text(utilities.manage_pages.web_server_admin_new_user.get_email(), email)
        UiActions.update_text(utilities.manage_pages.web_server_admin_new_user.get_user_name(), user)
        UiActions.update_text(utilities.manage_pages.web_server_admin_new_user.get_password(),password)
        UiActions.click(utilities.manage_pages.web_server_admin_new_user.get_create_user())

    @staticmethod
    @allure.step('verify number of users in table flow')
    def verify_number_of_users(number):
        if number>0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.server_admin_page.users_list)
            Verifications.verify_number_of_elements(utilities.manage_pages.web_server_admin.get_users_list(), number)

    @staticmethod
    @allure.step('search user from users table flow')
    def search_user(search_value):
        UiActions.clear(utilities.manage_pages.web_server_admin.get_search())
        UiActions.update_text(utilities.manage_pages.web_server_admin.get_search(), search_value)

    @staticmethod
    @allure.step('delete user from users table flow')
    def delete_user(by,value):
        if by =='user':
            UiActions.click(utilities.manage_pages.web_server_admin.get_user_by_user_name(value))
        elif by== 'index':
            UiActions.click(utilities.manage_pages.web_server_admin.get_user_by_index(value))
        UiActions.click(utilities.manage_pages.web_server_admin.get_delete())
        UiActions.click(utilities.manage_pages.web_server_admin.get_confirm_delete())

    @staticmethod
    @allure.step('go to home')
    def grafana_home(self):
        self.driver.get(get_data('Url'))


data= read_csv(get_data('Csv_Location'))
testdata =[
      (data[0][0], data[0][1]),
      (data[1][0], data[1][1]),
      (data[2][0], data[2][1])]






