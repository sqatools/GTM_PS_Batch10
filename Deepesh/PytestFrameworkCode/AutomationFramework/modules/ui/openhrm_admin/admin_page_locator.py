from selenium.webdriver.common.by import By

class admin_locator:

    admin_section_loc = (By.XPATH, "//span[text()='Admin']//parent::a")
    # Add user locators
    add_user_btn = (By.XPATH, " //button[normalize-space(.)='Add'] ")
    user_role_dropdown = (By.XPATH, "//label[text()='User Role']//parent::div/..//div[contains(text(), 'Select')]")
    status_dropdown = (By.XPATH, "//label[text()='Status']//parent::div/..//div[contains(text(), 'Select')]")
    employee_name_field = (By.XPATH, "//label[contains(text(), 'Employee Name')]//parent::div/..//input")
    username_name_field = (By.XPATH, "//label[contains(text(), 'Username')]//parent::div/..//input")
    user_password_field = (By.XPATH, "//label[text()='Password']//parent::div/..//input")
    confirm_password_field = (By.XPATH, "//label[text()='Confirm Password']//parent::div/..//input")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
