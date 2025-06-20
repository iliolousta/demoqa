from pages.web_tables import Tables


def add_test(browser):
    tables_page = Tables(browser)

    tables_page.visit()
    tables_page.btn_add.exist()
    assert tables_page.btn_add.click()
    assert not tables_page.btn_submit.click()
