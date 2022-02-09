from FinalProj1.constants import PASSWORD_LOGIN, USERNAME_LOGIN
from FinalProj1.locators.login_page_locators import LoginPageLocators
from FinalProj1.pages.admin_page import AdminPage
from FinalProj1.pages.base_page import BasePage


class LoginPage(BasePage):
    def try_to_login(self):
        username_field = self.find_element(LoginPageLocators.USERNAME_FIELD_LOCATOR)
        username_field.send_keys(USERNAME_LOGIN)
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(PASSWORD_LOGIN)
        login_btn = self.find_element(LoginPageLocators.LOGIN_BTN)
        login_btn.click()
        return AdminPage(self.driver, self.driver.current_url)
