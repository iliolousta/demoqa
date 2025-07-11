from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.button_small_modal.exist()
    assert modal_dialogs_page.button_large_modal.exist()

    modal_dialogs_page.button_small_modal.click()
    assert modal_dialogs_page.form.exist()
    modal_dialogs_page.close_small.click()
    assert not modal_dialogs_page.form.exist()

    modal_dialogs_page.button_large_modal.click()
    assert modal_dialogs_page.form.exist()
    modal_dialogs_page.close_large.click()
    assert not modal_dialogs_page.form.exist()
