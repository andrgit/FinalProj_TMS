from FinalProj1.locators.main_page_locators import MainPageLocators
from FinalProj1.pages.admin_page import AdminPage
from FinalProj1.pages.base_page import BasePage
from FinalProj1.pages.login_page import LoginPage


class MainPage(BasePage):
    URL = "http://localhost:8000/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_login_page(self):
        go_to_admin_btn = self.find_element(MainPageLocators.GO_TO_ADMIN_BTN)
        go_to_admin_btn.click()
        return LoginPage(self.driver, self.driver.current_url)

    def open_admin_page(self):
        go_to_admin_btn = self.find_element(MainPageLocators.GO_TO_ADMIN_BTN)
        go_to_admin_btn.click()
        return AdminPage(self.driver, self.driver.current_url)
