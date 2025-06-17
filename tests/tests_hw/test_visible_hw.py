import time

from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.lorem_ipsum.visible()
    accordion_page.heading.click()
    time.sleep(2)
    assert not accordion_page.lorem_ipsum.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.element_1.visible()
    assert not accordion_page.element_2.visible()
    assert not accordion_page.element_3.visible()
