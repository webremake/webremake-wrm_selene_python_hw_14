"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(scope='function', params=["desktop", "mobile"])
def browser_control(request):
    if request.param == "desktop":
        browser.config.hold_browser_open = True
        browser.config.browser_name = 'chrome'
        browser.config.base_url = 'https://github.com'
        browser.config.window_width = '1240'
        browser.config.window_height = '768'
        browser.config.timeout = 6.0
    if request.param == "mobile":
        browser.config.hold_browser_open = True
        browser.config.browser_name = 'chrome'
        browser.config.base_url = 'https://github.com'
        browser.config.window_width = '390'
        browser.config.window_height = '600'
        browser.config.timeout = 6.0

    yield
    browser.quit()


@pytest.mark.parametrize(
    "browser_control",
    [
        "desktop",
        pytest.param("mobile", marks=pytest.mark.skip(reason="Пропускаем тест для ширины экрана mobile"))
    ],
    indirect=True
)
def test_open_github_homepage_desktop(browser_control):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize(
    "browser_control",
    [
        "mobile",
        pytest.param("desktop", marks=pytest.mark.skip(reason="Пропускаем тест для ширины экрана desktop"))
    ],
    indirect=True
)
def test_open_github_homepage_mobile(browser_control):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('h1').should(have.exact_text('Sign in to GitHub'))
