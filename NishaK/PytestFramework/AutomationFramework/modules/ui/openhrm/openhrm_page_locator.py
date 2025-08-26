from selenium.webdriver.common.by import By


class openhrm_locator:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[contains(.,'Login')]")
