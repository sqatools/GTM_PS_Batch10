from selenium.webdriver.common.by import By


class openhrm_locator:
    username_feild=(By.NAME,"username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[contains(.,'Login')]")
