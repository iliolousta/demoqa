import time

from pages.web_tables import Tables

def test_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click_force()

    time.sleep(3)
    assert page_tables.no_data.exist()