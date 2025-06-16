from pages.base_page import BasePage
from components.components import WebElement

class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer > span', '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')
        self.center_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6', 'Please select an item from left to start practice.')




