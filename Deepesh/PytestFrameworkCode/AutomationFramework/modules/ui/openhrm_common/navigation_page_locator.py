from selenium.webdriver.common.by import By


class navigation_locator:
    # Sidebar module links
    admin_link = (By.XPATH, "//span[normalize-space()='Admin']")
    pim_link = (By.XPATH, "//span[normalize-space()='PIM']")
    leave_link = (By.XPATH, "//span[normalize-space()='Leave']")
    time_link = (By.XPATH, "//span[normalize-space()='Time']")
    recruitment_link = (By.XPATH, "//span[normalize-space()='Recruitment']")
    my_info_link = (By.XPATH, "//span[normalize-space()='My Info']")
    performance_link = (By.XPATH, "//span[normalize-space()='Performance']")
    dashboard_link = (By.XPATH, "//span[normalize-space()='Dashboard']")
    directory_link = (By.XPATH, "//span[normalize-space()='Directory']")
    maintenance_link = (By.XPATH, "//span[normalize-space()='Maintenance']")

    # Common page header
    page_header = (By.XPATH, "//header//h6")


