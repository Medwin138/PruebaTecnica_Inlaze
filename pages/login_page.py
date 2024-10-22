import os
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def open(self, url):
        self.driver.get(url)

    def capture_screenshot(self, action_name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
        return screenshot_path

    def login(self, email, password):
        try:
            email_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
            )
            password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
            signin_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")

            email_field.clear()
            email_field.send_keys(email)
            password_field.clear()
            password_field.send_keys(password)
            signin_button.click()

            self.capture_screenshot("login_attempt")
        except TimeoutException as e:
            print(f"Error during login: {str(e)}")
            self.capture_screenshot("login_error")
            raise

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//h2[normalize-space()='Welcome to Lorem'])[1]"))
            )
            return True
        except TimeoutException:
            return False

    def logout(self):
        try:
            img = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//img[@alt='Rengoku']"))
            )
            img.click()

            logout_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']"))
            )
            logout_button.click()

            self.capture_screenshot("logout_attempt")
        except TimeoutException as e:
            print(f"Error during logout: {str(e)}")
            self.capture_screenshot("logout_error")
            raise

    def is_logout_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Sign in']"))
            )
            return True
        except TimeoutException:
            return False

    def registro_usuario(self, full_name, email, password, repeat_password):
        try:
            registro = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/span/a"))
            )
            registro.click()

            full_name_field = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='full-name']"))
            )
            full_name_field.send_keys(full_name)

            email_field = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
            )
            email_field.send_keys(email)

            password_field = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
            )
            password_field.send_keys(password)

            repeat_password_field = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='confirm-password']"))
            )
            repeat_password_field.send_keys(repeat_password)

            btn_signup = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up']"))
            )
            btn_signup.click()

            self.capture_screenshot("registration_attempt")
        except TimeoutException as e:
            print(f"Error during registration: {str(e)}")
            self.capture_screenshot("registration_error")
            raise

    def is_registration_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='ml-3 text-sm font-normal'])[1]"))
            )
            return True
        except TimeoutException:
            return False
