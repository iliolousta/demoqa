import time

from selenium.webdriver.ie.webdriver import WebDriver

from pages.web_tables import Tables


def test_form(browser):
    tables_page = Tables(browser)
    first_name = 'test'
    last_name = 'testov'
    email = 'test@test.com'
    age = '28'
    salary = '100000'
    department = 'quality'


    tables_page.visit()
    assert tables_page.btn_add.exist()
    tables_page.btn_add.click()
    time.sleep(2)
    tables_page.btn_submit.click()
    assert tables_page.form.exist()

    tables_page.form_first_name.send_keys(first_name)
    tables_page.form_last_name.send_keys(last_name)
    tables_page.form_email.send_keys(email)
    tables_page.form_age.send_keys(age)
    tables_page.form_salary.send_keys(salary)
    tables_page.form_department.send_keys(department)
    tables_page.btn_submit.click()
    assert not tables_page.form.exist()
    time.sleep(2)

    assert tables_page.row_4_first_name.get_text() == first_name
    assert tables_page.row_4_last_name.get_text() == last_name
    assert tables_page.row_4_email.get_text() == email
    assert tables_page.row_4_age.get_text() == age
    assert tables_page.row_4_salary.get_text() == salary
    assert tables_page.row_4_department.get_text() == department

    browser.set_window_size(1500, 1000)
    tables_page.row_4_edit.click()
    time.sleep(2)
    assert tables_page.row_4_form.exist()
    tables_page.form_first_name.clear()
    time.sleep(2)
    tables_page.form_first_name.send_keys('QAEngineer')
    tables_page.btn_submit.click()
    assert tables_page.row_4_first_name.get_text() == 'QAEngineer'
    tables_page.row_4_delete.click()
    time.sleep(2)

    assert tables_page.row_4_first_name.get_text() == ' '
    assert tables_page.row_4_last_name.get_text() == ' '
    assert tables_page.row_4_email.get_text() == ' '
    assert tables_page.row_4_age.get_text() == ' '
    assert tables_page.row_4_salary.get_text() == ' '
    assert tables_page.row_4_department.get_text() == ' '


