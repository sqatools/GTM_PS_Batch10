from selenium.webdriver.common.by import By


class admin_locator:

    choose_admin = (By.XPATH, "//span[text()='Admin']")
    # Add User
    add_user = (By.XPATH, "//div[contains(@class,'orangehrm-header')]//button[@type='button']")
    select_dd = (By.XPATH, "//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][1]")
    select_admin_dd = (By.XPATH, "//div[@role='option']//span[text()='Admin']")
    e_name = (By.XPATH, "//input[contains(@placeholder,'Type for')]")
    select_employee = (By.XPATH, "//div[@class='oxd-autocomplete-option']")
    status = (By.XPATH, "//label[text()='User Role']//following::div[@class='oxd-select-wrapper'][2]")
    e_status = (By.XPATH, "//span[text()='Enabled']")
    e_username = (By.XPATH, "//label[text()='Username']//following::input[1]")
    e_password = (By.XPATH, "//label[text()='Password']//following::input[1]")
    c_password = (By.XPATH, "//label[text()='Password']//following::input[2]")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")

    # delete User
    s_username = (By.XPATH, "//label[text()='Username']//following::input[contains(@class,'oxd-input')]")
    search_user = (By.XPATH, "//button[normalize-space()='Search']")
    delete1_user = (By.XPATH, "//div[text()='user1_data']//following::div//i[@class='oxd-icon bi-trash']")
    delete2_user = (By.XPATH, "//div[@class='orangehrm-modal-footer']//button[@type='button'][2]")
    reset = (By.XPATH, "//button[normalize-space()='Reset']")

    # Job Section
    admin_job = (By.XPATH, "//span[text()='Job ']")
    job_title = (By.XPATH, "//a[text()='Job Titles']")
    add_title = (By.XPATH, "//button[normalize-space()='Add']")
    add_jobtitle = (By.XPATH, "//label[text()='Job Title']//following::input[contains(@class,'oxd-input')]")
    add_desc = (By.XPATH, "//textarea[@placeholder='Type description here']")
    browse = (By.XPATH, "//input[@type='file']")
    # save_button1 = (By.XPATH,"//button[text()=' Save ']")

    # Pay Grade Section
    select_pay_grades = (By.XPATH, "//a[text()='Pay Grades']")
    # add_grade = (By.XPATH, "//button[text()=' Add ']")
    grade_name = (By.XPATH, "//label[text()='Name']//following::input")
    # save_button = (By.XPATH, "//button[text()=' Save ']")
    add_currency = (By.XPATH, "//button[text()=' Add ']")
    currency_dd = (By.XPATH, "//label[text()='Currency']//following::i[1]")
    select_currency = (By.XPATH, "//div/span[text()='INR - Indian Rupee']")
    min_salary = (By.XPATH, "//label[text()='Minimum Salary']//following::input[1]")
    max_salary = (By.XPATH, "//label[text()='Minimum Salary']//following::input[2]")
    save_currency = (By.XPATH, "//label[text()='Maximum Salary']//following::button[@type='submit']")

    # job category section
    select_jobcategory = (By.XPATH, "//a[text()='Job Categories']")
    add_name = (By.XPATH, "//label[text()='Name']//following::input")

    # Organization Section
    select_organization = (By.XPATH, "//span[text()='Organization ']")
    general_info = (By.XPATH, "//a[text()='General Information']")
    edit = (By.XPATH, "//label[text()='Edit']//parent::div")
    register_no = (By.XPATH, "//form[contains(@class,'oxd-form')]//label[text()='Registration Number']/following::input[1]")

    # location section
    location = (By.XPATH, "//a[text()='Locations']")
    Name = (By.XPATH, "//label[text()='Name']//following::input[1]")
    City = (By.XPATH, "//label[text()='City']//following::input[1]")
    State = (By.XPATH, "//label[text()='State/Province']//following::input[1]")
    pincode = (By.XPATH, "//label[text()='Zip/Postal Code']//following::input[1]")
    country_dd = (By.XPATH, "//div[text()='-- Select --']")
    select_country = (By.XPATH, "//span[text()='India']")
    phone = (By.XPATH, "//label[text()='Phone']//following::input[1]")
    address = (By.XPATH, "//label[text()='Address']//following::textarea[1]")

    # Skills
    select_qualification = (By.XPATH, "//span[normalize-space()='Qualifications']")
    select_skill = (By.XPATH, "//a[normalize-space()='Skills']")
    skill_desc = (By.XPATH, "//label[text()='Description']//following::textarea")

    # Education
    select_edu = (By.XPATH, "//a[text()='Education']")
    level = (By.XPATH, "//label[text()='Level']//following::input[1]")

    # languages
    select_lang = (By.XPATH, "//a[text()='Languages']")
