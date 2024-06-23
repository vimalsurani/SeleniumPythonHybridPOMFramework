
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_textbox_id = "input-email"
    password_textbox_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email(self, email_address):
        self.type_into_element(email_address, "email_address_textbox_id", self.email_address_textbox_id)

    def enter_password(self, password):
        self.type_into_element(password, "password_textbox_id", self.password_textbox_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def login_to_application(self, email_address, password):
        self.enter_email(email_address)
        self.enter_password(password)
        return self.click_on_login_button()

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath", self.warning_message_xpath)
