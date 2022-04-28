from model.contact import Contact
from selenium.webdriver.support.select import Select
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

# Create new contact
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

    def create_in_group(self, сontact, group_name):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form_with_group(сontact, group_name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
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

    def fill_contact_form_with_group(self, Contact, group_name):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
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

    def fill_contact_form_for_replace_in_group(self, group_name):
        wd = self.app.wd
        my_select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[5]"))
        my_select.select_by_visible_text(group_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

# Modify first contact

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

# Modify contact by index

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

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # open modification form
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']/img" % id).click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_homepage()
        self.contact_cach = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def go_to_group_page(self, groupname):
        wd = self.app.wd
        self.app.open_home_page()
        my_select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        my_select.select_by_visible_text(groupname)

# Delete first contact

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.contact_cach = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.contact_cach = None

# Delete All contact

    def delete_all_contacts(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("// *[ @ id = 'MassCB']").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()
        self.contact_cach = None

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cach = None

    def get_contact_list(self):
        if self.contact_cach is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cach = []
            rows = wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[@name='entry']")
            for elements in rows:
                column = elements.find_elements_by_tag_name("td")
                firstname = column[2].text
                lastname = column[1].text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                all_phones = column[5].text
                all_emails = column[4].text
                address = column[3].text
                self.contact_cach.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                 all_emails_from_home_page=all_emails.replace(" ", ""),
                                                 all_phones_from_home_page=all_phones,
                                                 address=address))
        return list(self.contact_cach)

    def get_contact_list_in_group(self, group_name):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            my_select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
            my_select.select_by_visible_text(group_name)
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def add_in_group(self, group_name):
        wd = self.app.wd
        self.app.open_home_page()

        my_select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        my_select.select_by_visible_text(group_name)
        self.contact_cache = None

    def add_from_homepage_in_group(self, id, group_name):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        my_select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        my_select.select_by_visible_text(group_name)
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        column = row.find_elements_by_tag_name("td")[7]
        column.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        column = row.find_elements_by_tag_name("td")[6]
        column.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_to_group(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        # wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[4]/select/option[1]").click()
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def create_in_group(self, contact, group_name):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.fill_contact_form_for_group(contact, group_name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def replace_in_group(self, group_name):
        wd = self.app.wd
        self.app.open_home_page()
        self.fill_contact_form_for_replace_in_group(group_name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def remove_contact_from_group(self, id, group_number):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_group_by_rand_number(group_number, "remove")
        self.check_add_contact()
        x = 1 + 3

    def check_add_contact(self):
        wd = self.app.wd
        if wd.find_elements_by_name("selected[]") == 0:
            return None
        else:
            return len(wd.find_elements_by_name("selected[]"))

    def add_contact_to_group(self, contact_id, group_number):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        # rand_number = randrange(int((lambda x: (x-2)/2)(len(wd.find_elements_by_tag_name("option")))))
        self.select_group_by_rand_number(group_number, "addition")
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def select_group_by_rand_number(self, group_number, mode):
        wd = self.app.wd
        if mode == "remove":
            wd.find_element_by_xpath("//form[@id='right']/select//option[{0}]".format(group_number)).is_selected()
            wd.find_element_by_xpath("//form[@id='right']/select//option[{0}]".format(group_number)).click()
            count = 0
            while wd.current_url.endswith("/?group="):
                count += 1
                wd.find_element_by_xpath(
                    "//form[@id='right']/select//option[{0}]".format(group_number + count)).is_selected()
                wd.find_element_by_xpath("//form[@id='right']/select//option[{0}]".format(group_number + count)).click()
        elif mode == "addition":
            wd.find_element_by_xpath("//div[@class='right']/select//option[{0}]".format(group_number)).is_selected()
            wd.find_element_by_xpath("//div[@class='right']/select//option[{0}]".format(group_number)).click()

    def clean_contact(self, contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), home=contact.home.strip(),
                       mobile=contact.mobile.strip(), work=contact.work.strip(),
                       phone2=contact.phone2.strip(), email=contact.email, email2=contact.email2, email3=contact.email3)

    def create_contact_if_it_not_exist(self, contact):
        wd = self.app.wd
        if self.count() == 0:
            self.create(contact)

    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_by_id_for_add_contact(group_id)
        # submit adding
        wd.find_element_by_css_selector("[value='Add to']").click()
        # self.back_to_group_page()
        self.app.open_home_page()
        self.contact_cache = None

    def add_contact_to_some_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_from_some_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_value(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()
        self.contact_cache = None



    def select_group_by_id_for_add_contact(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group_id)

    def back_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[contains(text(), "group page ")]').click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_group_by_id_for_delete_contact(group_id)
        self.select_contact_by_id(contact_id)
        # submit adding
        wd.find_element_by_name("remove").click()
        self.back_to_group_page()
        self.contact_cache = None

    def select_group_by_id_for_delete_contact(self, id):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_value(id)

    def add_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact.id)
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_visible_text(group.name.strip())
        wd.find_element_by_name("add").click()

    def del_all_contacts_in_group(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='MassCB']").click()
        wd.find_element_by_name("remove").click()

