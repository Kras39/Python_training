from selenium.webdriver.support.select import Select
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

# Create new conact
    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        # fill in firstname
        self.fill_contact_form(contact)
        # submit_contact_creation
        wd.find_element_by_name("submit").click()
        self.return_to_homepage()
        self.contact_cach = None

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
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cach = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.contact_cach = None

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
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def add_first_contact_to_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_name("to_group").click()
        # wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[4]/select").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[4]/select/option[1]").click()
        wd.find_element_by_name("add").click()

    contact_cach = None

    def get_contact_list(self):
        if self.contact_cach is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cach=[]
            rows = wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[@name='entry']")
            for elements in rows:
                column = elements.find_elements_by_tag_name("td")
                firstname = column[2].text
                lastname = column[1].text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cach.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cach)




