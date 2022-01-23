# class Locator:
#     XPATH_USERNAME = '//*[@id="user-name"]'
#     XPATH_PASSWORD = '//*[@id="password"]'
#     XPATH_LOGIN = '//*[@id="login-button"]'



class Homepage():
    XPATH_APP_LOGO = '/html/body/header/nav/div/a/img'
    XPATH_HOME_LINK = '/html/body/header/nav/div/div/ul/li[1]/a'
    XPATH_VIEW_DOCTORS_BUTTON = '/html/body/section[2]/div/div/div/div/div[2]/a'
    XPATH_SIGN_IN = '/html/body/footer/div/div/div[3]/div/ul/li[1]/a'

    XPATH_DOCTOR = '/html/body/header/nav/div/div/ul/li[3]/a'
    XPATH_DOCTOR_SIGN_UP_DROPDOWN = '/html/body/header/nav/div/div/ul/li[3]/ul/li[2]/a'
    patient_sign_up_dropdown = '/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a'
    patient_id = 'dropdown02'

class Doctor_register():
    name_box = '/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input'
    email_box = '/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input'
    phone_box = '/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input'
    password_box = '/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input'
    re_password_box = '/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input'
    submit_button = '/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input'

class Doctor_homepage():
    add_prescription = '/html/body/section[2]/div/div[2]/div/div[4]/form/input'
    icon = '/html/body/header/nav/div/div/ul/li[2]/a'
    logout = '/html/body/header/nav/div/div/ul/li[2]/ul/li[5]/a'
    personal_profile = '/html/body/section[2]/div/div[2]/div/div[3]/form/input'
    prescribe_patient = '/html/body/section[2]/div/div[2]/div/div[4]/form/input'
    medicines = '/html/body/section[2]/div/div[2]/div/div[2]/input'
    registered_patients = '/html/body/section[2]/div/div[2]/div/div[1]/input'



class Login():
    email = '/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input'
    password = '/html/body/section[2]/div/div/div/form/div[1]/div[5]/div/input'
    submit_button = '/html/body/section[2]/div/div/div/form/div[2]/input'


class Patient_homepage():
    icon = '/html/body/header/nav/div/div/ul/li[2]/a'
    logout = '/html/body/header/nav/div/div/ul/li[2]/ul/li[5]/a'
    update_medical_details = '/html/body/header/nav/div/div/ul/li[2]/ul/li[4]/a'
    view_doctors = '/html/body/section[2]/div/div[2]/div/div[1]/input'
    view_profile = '/html/body/section[2]/div/div[2]/div/div[2]/form/input'


class Patient_register():
    name = '/html/body/section[2]/div/div/div/form/div[1]/div[1]/div/input'
    relative_name = '/html/body/section[2]/div/div/div/form/div[1]/div[3]/div/input'
    email = '/html/body/section[2]/div/div/div/form/div[1]/div[7]/div/input'
    phone = '/html/body/section[2]/div/div/div/form/div[1]/div[2]/div/input'
    ailments = '/html/body/section[2]/div/div/div/form/div[1]/div[9]/div/input'
    password = '/html/body/section[2]/div/div/div/form/div[1]/div[10]/div/input'
    re_password = '/html/body/section[2]/div/div/div/form/div[1]/div[11]/div/input'
    relative_phone = '/html/body/section[2]/div/div/div/form/div[1]/div[4]/div/input'
    dob = '/html/body/section[2]/div/div/div/form/div[1]/div[6]/div/input'
    address = '/html/body/section[2]/div/div/div/form/div[1]/div[8]/div/input'
    submit = '/html/body/section[2]/div/div/div/form/div[2]/input'


class Add_prescription():
    date = '/html/body/section[2]/div/div/div/form/div[2]/div[2]/div/input'
    next_visit = '/html/body/section[2]/div/div/div/form/div[2]/div[3]/div/input'
    reason = '/html/body/section[2]/div/div/div/form/div[2]/div[4]/div/input'
    doctor_notes = '/html/body/section[2]/div/div/div/form/div[2]/div[5]/div/input'
    submit = '/html/body/section[2]/div/div/div/form/div[3]/input'


class Update_medical_details():
    medical_history = '/html/body/section[2]/div/div[2]/div/form/div[1]/div/div[11]/div/input'
    submit = '/html/body/section[2]/div/div[2]/div/form/div[2]/input'

