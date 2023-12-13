import pytest
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    assert answer.text == f'Hello, {testdata["login"]}'


def test_step_3(site, select_input_login, select_input_password, select_input_button, select_create_button,
                select_post_title, select_save_button, select_input_title, select_input_description,
                select_input_content):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn_1 = site.find_element('css', select_input_button)
    btn_1.click()
    btn_2 = site.find_element('xpath', select_create_button)
    btn_2.click()
    input3 = site.find_element('xpath', select_input_title)
    input3.send_keys('My new test post')
    input4 = site.find_element('xpath', select_input_description)
    input4.send_keys('Test!')
    input5 = site.find_element('xpath', select_input_content)
    input5.send_keys('Test @_@')
    btn_3 = site.find_element('xpath', select_save_button)
    btn_3.click()
    answer = site.find_element('css', select_post_title)
    assert answer.text == 'My new test post'


if __name__ == '__main__':
    pytest.main(['-vv'])
