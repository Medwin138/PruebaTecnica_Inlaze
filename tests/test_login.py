import pytest
import pytest_html

from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_successful(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")
    login_page.login("juan.perez@example.com", "Password123!")

    assert login_page.is_login_successful(), "El login no fue exitoso."

    screenshot_path = login_page.capture_screenshot("login_successful")
    request.node.user_properties.append(("screenshot", screenshot_path))

def test_logout_successful(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")
    login_page.login("juan.perez@example.com", "Password123!")

    login_page.logout()
    assert login_page.is_logout_successful(), "El logout no fue exitoso."

    screenshot_path = login_page.capture_screenshot("logout_successful")
    request.node.user_properties.append(("screenshot", screenshot_path))

def test_register_successful(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")
    login_page.registro_usuario("Emilio Perez", "emilio.perez@example.com", "Password123!", "Password123!")

    assert login_page.is_registration_successful(), "El registro no fue exitoso."

    screenshot_path = login_page.capture_screenshot("registration_successful")
    request.node.user_properties.append(("screenshot", screenshot_path))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['setup']
        screenshot_path = driver.save_screenshot(f"screenshots/{item.nodeid.replace('::', '_')}.png")
        if screenshot_path:
            extra = getattr(rep, 'extra', [])
            rep.extra = extra + [pytest_html.extras.image(screenshot_path)]
