import allure
import pytest

from extensions.verifications import Verifications
from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
@pytest.mark.usefixtures('init_db_connection')
class Test_Web_DB:
    @allure.title('Test01: Login to grafana via DB')
    @allure.description('This test verify login using elements taken from database')
    def test_verify_login_db(self):
        DBFlows.login_grafana_via_db()
        WebFlows.verify_grafana_title('Welcome to Grafana')
