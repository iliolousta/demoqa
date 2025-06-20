from wsproto.handshake import WEBSOCKET_VERSION

from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.result_name = WebElement(driver, '#name')
        self.result_address = WebElement(driver, '#output #currentAddress')

