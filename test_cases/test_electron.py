import allure
import pytest

from extensions.verifications import Verifications
from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class Test_Electron:
    @allure.title('Test01: Add And Verify New Task')
    @allure.description('This test adds a new task and verifies it in the list of tasks')
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task_flow('Learn python')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 1)

    @allure.title('Test02: Add And Verify New Tasks')
    @allure.description('This test adds a new tasks and verifies them  in the list of tasks')
    def test_add_and_verify_new_tasks(self):
        ElectronFlows.add_new_task_flow('Learn js')
        ElectronFlows.add_new_task_flow('Learn java')
        ElectronFlows.add_new_task_flow('Learn c#')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3)

    def teardown_method(self):
        ElectronFlows.empty_list_flow()









