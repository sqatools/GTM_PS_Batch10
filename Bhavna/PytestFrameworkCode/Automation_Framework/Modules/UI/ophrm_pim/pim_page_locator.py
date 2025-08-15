from selenium.webdriver.common.by import By

class pim_locator:

    choose_PIM = (By.XPATH,"//span[normalize-space()='PIM']")
    add = (By.XPATH,"//button[normalize-space()='Add']")
    first_name = (By.NAME,"firstName")
    last_name = (By.NAME,"lastName")
    save = (By.XPATH,"//button[normalize-space()='Save']")
    select_cont_dls = (By.XPATH,"//a[normalize-space()='Contact Details']")
    street1 = (By.XPATH,"//label[normalize-space()='Street 1']//following::input[1]")
    street2 = (By.XPATH,"//label[normalize-space()='Street 2']//following::input[1]")
    city = (By.XPATH,"//label[normalize-space()='City']//following::input[1]")
    state = (By.XPATH,"//label[normalize-space()='State/Province']//following::input[1]")
    postal_code = (By.XPATH,"//label[normalize-space()='Zip/Postal Code']//following::input[1]")
    country_dd = (By.XPATH,"//label[normalize-space()='Country']//following::div[1]")
    select_country = (By.XPATH,"//label[normalize-space()='Country']//following::span[normalize-space()='India']")
    mobile = (By.XPATH,"//label[normalize-space()='Mobile']//following::input[1]")



