from pages.base_page import BasePage
from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.button.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    base_page = DemoQa(browser)

    modal_dialogs_page.visit()
    browser.refresh()
    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert base_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)