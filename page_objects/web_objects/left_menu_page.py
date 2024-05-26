from selenium.webdriver.common.by import By

grafana= (By.CSS_SELECTOR, "a[aria-label='Home']")
search_dashboards= (By.CSS_SELECTOR, "a[aria-label='Search dashboards']")
create= (By.CSS_SELECTOR, "a[aria-label='Create']")
dashboards= (By.CSS_SELECTOR, "a[aria-label='Dashboards']")
explore= (By.CSS_SELECTOR, "a[aria-label='Explore']")
alerting= (By.CSS_SELECTOR, "a[aria-label='Alerting']")
configuration= (By.CSS_SELECTOR, "a[aria-label='Configuration']")
server_admin= (By.CSS_SELECTOR, "a[aria-label='Server Admin']")
admin= (By.CSS_SELECTOR, "a[aria-label='admin']")
help= (By.CSS_SELECTOR, "a[aria-label='Help']")









class LeftMenuPage():
    def __init__(self, driver):
        self.driver = driver

    def get_grafana(self):
        return self.driver.find_element(grafana[0],grafana[1])

    def get_search_dashboards(self):
        return self.driver.find_element(search_dashboards[0],search_dashboards[1])

    def get_create(self):
        return self.driver.find_element(create[0],create[1])

    def get_dashboards(self):
        return self.driver.find_element(dashboards[0],dashboards[1])

    def get_explore(self):
        return self.driver.find_element(explore[0],explore[1])

    def get_alerting(self):
        return self.driver.find_element(alerting[0],alerting[1])

    def get_configuration(self):
        return self.driver.find_element(configuration[0],configuration[1])

    def get_server_admin(self):
        return self.driver.find_element(server_admin[0],server_admin[1])

    def get_admin(self):
        return self.driver.find_element(admin[0],admin[1])

    def get_Help(self):
        return self.driver.find_element(help[0],help[1])




