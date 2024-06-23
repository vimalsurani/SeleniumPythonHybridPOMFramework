from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):
    @pytest.mark.parametrize("emai_address, password",
                             ExcelUtils.get_data_from_excel("ExcelFiles/TutorialsNinja.xlsx", "LoginTest"))
    def test_with_valid_credentials(self,emai_address,password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(emai_address,password)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_with_invalid_email_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_timestamp(), "Abc123456789")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(
            expected_warning_message)

    def test_with_valid_email_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("vimalpatel7449@gmail.com", "123456789")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(
            expected_warning_message)

    def test_without_entering_any_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(
            expected_warning_message)
