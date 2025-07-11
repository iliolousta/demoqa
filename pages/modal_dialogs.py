from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.button = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.button_small_modal = WebElement(driver, '#showSmallModal')
        self.button_large_modal = WebElement(driver, '#showLargeModal')
        self.form = WebElement(driver, 'body > div.fade.modal.show')
        self.close_large = WebElement(driver, '#closeLargeModal')
        self.close_small = WebElement(driver, '#closeSmallModal')
