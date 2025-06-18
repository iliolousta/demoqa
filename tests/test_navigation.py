from pages.base_page import BasePage
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    base_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    base_page.visit()
    base_page.btn_elements.click()

    base_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()