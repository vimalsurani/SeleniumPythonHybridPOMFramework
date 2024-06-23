from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.ID, locator_value))
            )
        elif locator_name.endswith("_name"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.NAME, locator_value))
            )
        elif locator_name.endswith("_class_name"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, locator_value))
            )
        elif locator_name.endswith("_link_text"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.LINK_TEXT, locator_value))
            )
        elif locator_name.endswith("_xpath"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.XPATH, locator_value))
            )
        elif locator_name.endswith("css"):
            element = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator_value))
            )
        return element
