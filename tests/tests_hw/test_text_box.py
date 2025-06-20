from pages.text_box import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('tester')
    text_box_page.current_address.send_keys('spb')
    text_box_page.btn_submit.click_force()
    assert text_box_page.result_name.get_text() == 'Name:tester'
    assert text_box_page.result_address.get_text() == 'Current Address :spb'