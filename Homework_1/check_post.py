import yaml
import requests

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = 'https://test-stand.gb.ru/api/posts'
    get = requests.get(url=path, headers={"X-Auth-Token": data['token']})
    if get.status_code == 200:
        return get.json()


if __name__ == '__main__':
    print(get_post(data['token']))
