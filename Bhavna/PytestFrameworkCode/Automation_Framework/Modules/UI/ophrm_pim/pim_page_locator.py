from selenium.webdriver.common.by import By


class pim_locator:

    choose_PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    add = (By.XPATH, "//button[normalize-space()='Add']")
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    save = (By.XPATH, "//button[normalize-space()='Save']")

    # contact details
    select_cont_dls = (By.XPATH, "//a[normalize-space()='Contact Details']")
    street1 = (By.XPATH, "//label[normalize-space()='Street 1']//following::input[1]")
    street2 = (By.XPATH, "//label[normalize-space()='Street 2']//following::input[1]")
    city = (By.XPATH, "//label[normalize-space()='City']//following::input[1]")
    state = (By.XPATH, "//label[normalize-space()='State/Province']//following::input[1]")
    postal_code = (By.XPATH, "//label[normalize-space()='Zip/Postal Code']//following::input[1]")
    country_dd = (By.XPATH, "//label[normalize-space()='Country']//following::div[1]")
    select_country = (By.XPATH, "//label[normalize-space()='Country']//following::span[normalize-space()='India']")
    mobile = (By.XPATH, "//label[normalize-space()='Mobile']//following::input[1]")

    # emergency contact
    select_emerg_cnt = (By.XPATH, "//a[normalize-space()='Emergency Contacts']")
    add_cont = (By.XPATH, "//h6[text()='Assigned Emergency Contacts']//following::button[1]")
    Name = (By.XPATH, "//label[normalize-space()='Name']//following::input[1]")
    relationship = (By.XPATH, "//label[normalize-space()='Relationship']//following::input[1]")

    # job details
    select_job = (By.XPATH, "//a[normalize-space()='Job']")
    join_date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    job_title_dd = (By.XPATH, "//label[normalize-space()='Job Title']//following::i[1]")
    select_job_title = (By.XPATH,"//span[normalize-space()='HR Associate']")
    job_category_dd = (By.XPATH, "//label[normalize-space()='Job Category']//following::i[1]")
    job_category = (By.XPATH, "//span[normalize-space()='Officials and Managers']")
    sub_unit_dd = (By.XPATH, "//label[normalize-space()='Sub Unit']//following::i[1]")
    sub_unit = (By.XPATH, "//span[normalize-space()='Administration']")
    location_dd = (By.XPATH, "//label[normalize-space()='Location']//following::i[1]")
    location = (By.XPATH, "//span[normalize-space()='HQ - CA, USA']")

    # attachment
    add_attach = (By.XPATH, "//button[normalize-space()='Add']")
    file_input = (By.XPATH, "//input[@type='file']")
    # browse = (By.XPATH,"//div[normalize-space()='Browse']")
