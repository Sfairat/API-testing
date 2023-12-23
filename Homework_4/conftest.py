import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from zeep import Client, Settings


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


@pytest.fixture(scope="session")
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def post_title_list():
    post = requests.post(url=testdata["path"], data={"username": testdata["username"], "password": testdata["pass"]})
    if post.status_code == 200:
        token = (post.json()["token"])
        get_post = requests.get(url=testdata["post_path"], headers={"X-Auth-Token": token})
        title_list = [item["title"] for item in get_post.json()["data"]]
        return title_list


@pytest.fixture()
def yandex_check_text():
    settings = Settings(strict=False)
    client = Client(wsdl=testdata['path_yandex'], settings=settings)
    check = client.service.checkText(testdata['yandex_text'])[0]['s']
    return check
