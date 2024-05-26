#web objects
import test_cases.conftest
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.login_page import LoginPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.left_menu_page import LeftMenuPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.server_admin_menu_page import ServerAdminMenuPage
from page_objects.web_objects.server_admin_new_user_page import ServerAdminNewUserPage
from page_objects.web_objects.server_admin_page import ServerAdminPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage
from test_cases import conftest

#web objects
web_login=None
web_main=None
web_upper_menu=None
web_left_menu= None
web_server_admin_menu= None
web_server_admin= None
web_server_admin_new_user= None


#Mobile Objects
mobile_calculator= None
mobile_saved= None


#Electron Objects
electron_task = None

#Desktop Objects
standard_calc = None


class Manage_Pages:
    @staticmethod
    def init_web_pages():
        globals()['web_login']= LoginPage(test_cases.conftest.driver)
        globals()['web_main']= MainPage(test_cases.conftest.driver)
        globals()['web_upper_menu']=UpperMenuPage(test_cases.conftest.driver)
        globals()['web_left_menu']=LeftMenuPage(test_cases.conftest.driver)
        globals()['web_server_admin_menu']=ServerAdminMenuPage(test_cases.conftest.driver)
        globals()['web_server_admin']=ServerAdminPage(test_cases.conftest.driver)
        globals()['web_server_admin_new_user']=ServerAdminNewUserPage(test_cases.conftest.driver)


    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator']=CalculatorPage(conftest.driver)
        globals()['mobile_saved']=SavedPage(conftest.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conftest.driver)

    @staticmethod
    def init_dasktop_pages():
        globals()['standard_calc'] = StandardPage(conftest.driver)






