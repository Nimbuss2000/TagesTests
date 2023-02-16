from pathlib import Path
import pytest
import requests
from page.base_page import BasePageClass
from configs.config import base_url


path_to_expect_data = Path(r"C:\PythonProjects2\TagesTests\configs\except_data.json")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chose browser: chrome/firefox")
    parser.addoption("--device", action="store", default="pc", help="chose device: pc/mobile")


@pytest.fixture
def get_status_code():
    def get_code(url):
        return requests.get(url).status_code
    return get_code


@pytest.fixture(scope='class')
def work_driver(request, pytestconfig):
    url = base_url
    browser = request.config.option.browser

    mark = pytestconfig.getoption('-m')
    if mark == 'mobile':
        device = 'mobile'
    else:
        device = 'desktop'
    #
    # markers = request.node.own_markers
    # for marker in markers:
    #     if marker == 'mobile':
    #         print(marker.name)

    base_page = BasePageClass(url, browser, device)
    yield base_page
    del base_page
