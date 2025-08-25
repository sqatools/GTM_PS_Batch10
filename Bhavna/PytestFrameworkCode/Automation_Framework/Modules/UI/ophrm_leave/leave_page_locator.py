from selenium.webdriver.common.by import By


class LeaveLocator:

    choose_leave = (By.XPATH, "//span[normalize-space()='Leave']")
    # Add Leave Entitlement
    entitlement = (By.XPATH, "//span[normalize-space()='Entitlements']")
    add_entitlement = (By.XPATH, "//a[normalize-space()='Add Entitlements']")
    multiple_employee = (By.XPATH, "//label[normalize-space()='Multiple Employees']")
    location_dd = (By.XPATH, "//label[normalize-space()='Location']//following::div[1]")
    location = (By.XPATH, "//span[normalize-space()='Texas R&D']")
    sub_unit_dd = (By.XPATH, "//label[normalize-space()='Sub Unit']//following::div[1]")
    sub_unit = (By.XPATH, "//span[normalize-space()='Quality Assurance']")
    leave_type_dd = (By.XPATH, "//label[normalize-space()='Leave Type']//following::div[1]")
    leave_type = (By.XPATH, "//span[normalize-space()='CAN - Personal']")
    entitle_day = (By.XPATH, "//label[normalize-space()='Entitlement']//following::input[1]")
    save = (By.XPATH, "//button[normalize-space()='Save']")
    confirm = (By.XPATH, "//button[normalize-space()='Confirm']")
    # Leave Entitlements
    employee_name = (By.XPATH, "//label[normalize-space()='Employee Name']//following::input[1]")
    select_employee = (By.XPATH, "//div[@class='oxd-autocomplete-option']")
    search = (By.XPATH, "//button[normalize-space()='Search']")


