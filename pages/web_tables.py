from components.components import WebElement
from pages.base_page import BasePage

class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'delete')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_edit = WebElement(driver, 'edit')

        self.table = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

        self.form = WebElement(driver, 'body > div.fade.modal.show')
        self.form_first_name = WebElement(driver, '#firstName')
        self.form_last_name = WebElement(driver, '#lastName')
        self.form_email = WebElement(driver, '#userEmail')
        self.form_age = WebElement(driver, '#age')
        self.form_salary = WebElement(driver, '#salary')
        self.form_department = WebElement(driver, '#department')

        self.row_4_first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.row_4_last_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.row_4_email = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.row_4_age = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)')
        self.row_4_salary = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)')
        self.row_4_department = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.row_4_edit = WebElement(driver, '#edit-record-4 > svg > path')
        self.row_4_form = WebElement(driver, 'body > div.fade.modal.show')

        self.row_4_delete = WebElement(driver, '#delete-record-4 > svg > path')

        self.first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1) > div.rt-resizable-header-content')
        self.last_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer > div.rt-resizable-header-content')
        self.age = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(3) > div.rt-resizable-header-content')
        self.email = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4) > div.rt-resizable-header-content')
        self.salary = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(5) > div.rt-resizable-header-content')
        self.department = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(6) > div.rt-resizable-header-content')

        self.title_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1)')
        self.attributes = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4)')

