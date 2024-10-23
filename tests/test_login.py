import os

import pytest
import pytest_html
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs['setup']
        screenshot_path = f"screenshots/{item.nodeid.replace('::', '_')}.png"
        driver.save_screenshot(screenshot_path)
        if os.path.exists(screenshot_path):
            extra = getattr(rep, 'extra', [])
            rep.extra = extra + [pytest_html.extras.image(screenshot_path)]

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


# Test para validación de nombre
def test_register_name_validation(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")

    login_page.registro_usuario_error("Juan", "test@example.com", "Password123!", "Password123!")

    assert login_page.is_register_button_enabled(), "El botón de registro no debería estar habilitado con un solo nombre."


# def test_register_email_uniqueness(setup, request):
#     login_page = LoginPage(setup)
#     login_page.open("https://test-qa.inlaze.com/login")
#
#     # Intentamos registrar un usuario con un correo que ya existe
#     login_page.registro_usuario("Juan Perez", "juan.perez@example.com", "Password123!", "Password123!")
#
#     # Localizar el mensaje de error
#     error_message = login_page.get_error_message()  # Supongamos que hay un método para obtener el mensaje de error
#
#     # Verificar que el mensaje de error aparezca
#     assert "El correo electrónico ya está registrado" in error_message, "El mensaje de error por correo duplicado no se mostró correctamente"


def test_register_password_validation(setup):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")

    # Ingresar datos incorrectos para que el botón quede deshabilitado
    login_page.registro_usuario_error("Emilio Perez", "emilio.perez@example.com", "pass", "pass")

    # Verifica si el botón está deshabilitado
    assert login_page.is_register_button_disabled() == True, "El botón de registro debería estar deshabilitado debido a datos incorrectos."

def test_register_required_fields(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")

    login_page.registro_usuario_error("", "test@example.com", "Password123!", "Password123!")  # Campo de nombre vacío

    assert login_page.is_register_button_disabled() == True, "El botón de registro debería estar deshabilitado debido a datos incompletos."

def test_register_password_mismatch(setup, request):
    login_page = LoginPage(setup)
    login_page.open("https://test-qa.inlaze.com/login")

    login_page.registro_usuario_error("Emilio Perez", "emilio.perez@example.com", "Password123!", "Password1234!")

    assert login_page.is_register_button_disabled(), "El botón de registro debería estar inactivo para contraseñas no coincidentes."
    assert "Passwords do not match" in login_page.get_error_message(), "No se mostró el mensaje de error para contraseñas no coincidentes."
