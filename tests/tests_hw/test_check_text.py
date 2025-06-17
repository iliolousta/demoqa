from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
#
# def test_check_test(browser):
#     demo_qa_page = DemoQa(browser)
#     elements_page = ElementsPage(browser)
#
#     demo_qa_page.visit()
#     demo_qa_page.footer.click()
#     assert demo_qa_page.footer.equal_text()
#
#     demo_qa_page.visit()
#     demo_qa_page.btn_elements.click()
#     assert elements_page.center_text.equal_text()
#
#     elements_page.visit()
#     assert elements_page.text_elements.equal_text()

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()