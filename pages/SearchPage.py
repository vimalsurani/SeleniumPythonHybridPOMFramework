from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    not_found_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text", self.valid_hp_product_link_text)

    def retrieve_not_found_product_message(self):
        return self.retrieve_element_text("not_found_product_message_xpath", self.not_found_product_message_xpath)
