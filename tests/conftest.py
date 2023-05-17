import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_control():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = '1024'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0
    yield
    ...

