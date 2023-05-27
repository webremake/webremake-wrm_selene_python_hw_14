"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(scope='function', params=["desktop", "mobile"])
def browser_control(request):
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 6.0
    if request.param == "desktop":
        browser.config.window_width = '1240'
        browser.config.window_height = '768'

    if request.param == "mobile":
        browser.config.window_width = '390'
        browser.config.window_height = '600'
    yield
    browser.quit()


@pytest.mark.parametrize("browser_control", ["desktop"], indirect=True)
def test_open_github_homepage_desktop(browser_control):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))


browser_with_window_width_390 = pytest.mark.parametrize("browser_control", ["mobile"], indirect=True)


@browser_with_window_width_390
def test_open_github_homepage_mobile(browser_control):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))
