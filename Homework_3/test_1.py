from testpage import OperationsHelper
import logging
import yaml
import pytest


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step_2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_button()
    testpage.enter_name('Alex')
    testpage.enter_email('example@mail.ru')
    testpage.enter_content('Test')
    testpage.click_contact_us_button()
    assert testpage.get_alert_text() == 'Form successfully submitted'


if __name__ == '__main__':
    pytest.main(['-vv'])
