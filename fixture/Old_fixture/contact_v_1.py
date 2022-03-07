from selenium.webdriver.support.select import Select

class ContactHelper_v_1:

    def __init__(self, app):
        self.app = app

# Create new conact
    def open_add_new(self):
        wd = self.app.wd
        # if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0:
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        # fill in firstname
        self.fill_contact_form(contact)
        # submit_contact_creation
        wd.find_element_by_name("submit").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nikename)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("/html/body/div/div[4]/form/select[1]//option[16]").is_selected():
            wd.find_element_by_xpath("/html/body/div/div[4]/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("/html/body/div/div[4]/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("/html/body/div/div[4]/form/select[2]//option[9]").click()
        self.change_field_value("byear", contact.byear)
        if not wd.find_element_by_xpath("/html/body/div/div[4]/form/select[3]//option[12]").is_selected():
            wd.find_element_by_xpath("/html/body/div/div[4]/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("/html/body/div/div[4]/form/select[4]//option[9]").is_selected():
            wd.find_element_by_xpath("/html/body/div/div[4]/form/select[4]//option[11]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            # wd.find_element_by_name(field_name).select_by_visible_text()
            # wd.find_element_by_name(field_name).send_keys(text)

# Modify first contact
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

# Delete contact
    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()

# Delete All contact
    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select all contact
        wd.find_element_by_xpath("// *[ @ id = 'MassCB']").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_add_new()
        return len(wd.find_elements_by_name("selected[]"))