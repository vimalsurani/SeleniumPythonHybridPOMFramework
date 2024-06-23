from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_textbox_id = "input-firstname"
    last_name_textbox_id = "input-lastname"
    register_email_address_textbox_id = "input-email"
    telephone_textbox_id = "input-telephone"
    register_password_textbox_id = "input-password"
    confirm_password_textbox_id = "input-confirm"
    agree_checkbox_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    subscribe_yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_xpath = "//div[@id='account-register']/div[1]"
    agree_privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_address_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name):
        self.type_into_element(first_name, "first_name_textbox_id", self.first_name_textbox_id)

    def enter_last_name(self, last_name):
        self.type_into_element(last_name, "last_name_textbox_id", self.last_name_textbox_id)

    def enter_register_email_address(self, email_address):
        self.type_into_element(email_address, "register_email_address_textbox_id",
                               self.register_email_address_textbox_id)

    def enter_telephone_number(self, telephone):
        self.type_into_element(telephone, "self.telephone_textbox_id", self.telephone_textbox_id)

    def enter_register_password(self, password):
        self.type_into_element(password, "register_password_textbox_id", self.register_password_textbox_id)

    def enter_confirm_password(self, confirm_password):
        self.type_into_element(confirm_password, "confirm_password_textbox_id", self.confirm_password_textbox_id)

    def select_agree_checkbox(self):
        self.element_click("agree_checkbox_name", self.agree_checkbox_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.element_click("subscribe_yes_radio_button_xpath", self.subscribe_yes_radio_button_xpath)

    def register_an_account(self, first_name, last_name, email_address, telephone, password, confirm_password,
                            yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_register_email_address(email_address)
        self.enter_telephone_number(telephone)
        self.enter_register_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning_message(self):
        return self.retrieve_element_text("duplicate_email_warning_message_xpath",
                                          self.duplicate_email_warning_message_xpath)

    def retrieve_agree_privacy_policy_warning_message(self):
        return self.retrieve_element_text("agree_privacy_policy_warning_message_xpath",
                                          self.agree_privacy_policy_warning_message_xpath)

    def retrieve_first_name_warning_message(self):
        return self.retrieve_element_text("first_name_warning_xpath", self.first_name_warning_xpath)

    def retrieve_last_name_warning_message(self):
        return self.retrieve_element_text("last_name_warning_xpath", self.last_name_warning_xpath)

    def retrieve_email_address_warning_message(self):
        return self.retrieve_element_text("email_address_warning_xpath", self.email_address_warning_xpath)

    def retrieve_telephone_warning_message(self):
        return self.retrieve_element_text("telephone_warning_xpath", self.telephone_warning_xpath)

    def retrieve_password_warning_message(self):
        return self.retrieve_element_text("password_warning_xpath", self.password_warning_xpath)

    def verify_warning_message(self, expected_privacy_policy_warning_text, expected_first_name_warning_text,
                               expected_last_name_warning_text, expected_email_warning_text,
                               expected_telephone_warning_text, expected_password_warning_text):
        actual_privacy_policy_warning_text = self.retrieve_agree_privacy_policy_warning_message()
        actual_first_name_warning_text = self.retrieve_first_name_warning_message()
        actual_last_name_warning_text = self.retrieve_last_name_warning_message()
        actual_email_warning_text = self.retrieve_email_address_warning_message()
        actual_telephone_warning_text = self.retrieve_telephone_warning_message()
        actual_password_warning_text = self.retrieve_password_warning_message()

        status = False

        if expected_privacy_policy_warning_text.__contains__(actual_privacy_policy_warning_text):
            if expected_first_name_warning_text.__eq__(actual_first_name_warning_text):
                if expected_last_name_warning_text.__eq__(actual_last_name_warning_text):
                    if expected_email_warning_text.__eq__(actual_email_warning_text):
                        if expected_telephone_warning_text.__eq__(actual_telephone_warning_text):
                            if expected_password_warning_text.__eq__(actual_password_warning_text):
                                status = True

        return status
