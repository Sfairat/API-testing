from testpage import OperationsHelper
import logging
import yaml
import pytest


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info('Test1 starting')
    testpage = OperationsHelper(browser)
    testpage.log_in('test', 'test')
    assert testpage.get_error_text() == '401'


def test_step_2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.log_in(testdata['login'], testdata['password'])
    assert testpage.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(browser, post_title_list):
    logging.info('Test3 starting')
    testpage = OperationsHelper(browser)
    testpage.log_in(testdata['username'], testdata['pass'])
    assert testpage.get_post_title_text() in post_title_list


def test_step_4(browser):
    logging.info('Test4 starting')
    testpage = OperationsHelper(browser)
    testpage.log_in(testdata['username'], testdata['pass'])
    testpage.click_create_post_button()
    testpage.enter_post_title('Another test post')
    testpage.enter_post_description('Test post description')
    testpage.enter_post_content('^=_=^')
    testpage.click_save_post_button()
    assert 'Test post description' in testpage.get_post_description_list()


def test_step_5(yandex_check_text):
    logging.info('Test5 starting')
    assert 'колбаса' in yandex_check_text


if __name__ == '__main__':
    pytest.main(['-vv'])

