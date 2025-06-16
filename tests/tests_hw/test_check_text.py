from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_test(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.footer.click()
    assert demo_qa_page.footer.equal_text()

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elements_page.center_text.equal_text()

