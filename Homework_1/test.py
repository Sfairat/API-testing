import pytest
from check_post import get_post


def test_check_post(token):
    id_check = 63613
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res


def test_create_post(token):
    description_check = 'Very cool post'
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['description'])
    assert description_check in res


if __name__ == '__main__':
    pytest.main(['-vv'])