import yaml
import requests
from check_post import get_login

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def create_post():
    path = data['post_path']
    post = requests.post(url=path, headers={"X-Auth-Token": data['token']},
                         data={'username': 'lldfgdh', 'password': '1743ab0424'},
                         params={'title': 'My new post',
                                 'description': 'Very cool post',
                                 'content': '^_^'})
    if post.status_code == 200:
        return post.json()['description']


if __name__ == '__main__':
    token = get_login()
    print(create_post())
