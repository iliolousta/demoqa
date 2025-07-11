from pages.web_tables import Tables


def test_sort(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    page_tables.first_name.click()
    assert page_tables.title_name.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-asc -cursor-pointer"

    page_tables.last_name.click()
    assert page_tables.title_name.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-desc -cursor-pointer"

    page_tables.age.click()
    assert page_tables.attributes.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"

    page_tables.email.click()
    assert page_tables.attributes.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-asc -cursor-pointer"

    page_tables.salary.click()
    assert page_tables.attributes.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"

    page_tables.department.click()
    assert page_tables.attributes.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"