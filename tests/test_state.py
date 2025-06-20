import time

from pages.form_page import FormPage


def test_state(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)