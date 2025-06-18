from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElement:

    def __init__(self, driver, locator=" ", text=" "):
        self.driver = driver
        self.locator = locator
        self.text = text

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def equal_text(self):
        if self.get_text() == self.text:
            return True
        return False

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)