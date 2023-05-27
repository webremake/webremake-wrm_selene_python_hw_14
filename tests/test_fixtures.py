"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture(scope='function',  autouse=True)
def browser_control():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 6.0


@pytest.fixture(scope='function')
def browser_window_width_1240():
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    yield
    browser.quit()


@pytest.fixture(scope='function')
def browser_window_width_390():
    browser.config.window_width = '390'
    browser.config.window_height = '600'
    yield
    browser.quit()


def test_open_github_homepage_desktop_in(browser_window_width_1240):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))


def test_open_github_homepage_mobile_in(browser_window_width_390):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))
