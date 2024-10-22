import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import datetime

@pytest.fixture(scope="module")
def setup():
    # Configura el navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Opcional: Ejecutar sin interfaz gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def pytest_html_results_table_row(report, cells):
    for prop in report.user_properties:
        if prop[0] == "screenshot":
            cells.append(f'<img src="{prop[1]}" style="max-width: 200px;"/>')

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is not None:
            # Captura de pantalla en caso de fallo
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.png")

            # Guarda la captura de pantalla utilizando el driver de la prueba
            driver = item.funcargs['setup']
            driver.save_screenshot(screenshot_path)  # Guarda la captura de pantalla
            item.user_properties.append(("screenshot", screenshot_path))  # Añade la captura al reporte
