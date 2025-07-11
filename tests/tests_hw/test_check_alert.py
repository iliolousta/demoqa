import time

from pages.alerts import Alerts


def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.btn_timer.exist()
    alert_page.btn_timer.click()
    time.sleep(7)
    assert alert_page.alert()
    alert_page.alert().accept()