import pytest
from selene import browser, have


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.hold_browser_open = True
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 6.0
    yield
    browser.quit()


@pytest.fixture(scope='function', params=["desktop", "mobile"])
def window_size(request):
    if request.param == "desktop":
        browser.config.window_width = '1240'
        browser.config.window_height = '768'
    elif request.param == "mobile":
        browser.config.window_width = '390'
        browser.config.window_height = '600'


def test_open_github_homepage_desktop(window_size):
    if browser.config.window_width == '390':
        pytest.skip("Пропускаем тест для ширины экрана mobile")
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))


def test_open_github_homepage_mobile(window_size):
    if browser.config.window_width == '1240':
        pytest.skip("Пропускаем тест для ширины экрана desktop")
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))
