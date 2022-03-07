# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from model.contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_add_new(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nikename)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_contacts(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new(wd)
        self.create_new_contact(wd, Contact(firstname="contact_1", middlename="contact_2", lastname="New Contact", nikename="NC", title="WP",
                company="New Company", address="Wood Street", home="123", mobile="456", work="789", fax="010",
                email="contact_1@gmail.com", email2="contact_2@gmail.com", email3="contact_3@gmail.com",
                homepage="www.contact.com", bday="1", bmonth="January", byear="1990", aday="1", amonth="January",
                ayear="2020", address2="Wood Street 2", phone2="1", notes="B2"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_add_empty_contacts(self):
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new(wd)
        self.create_new_contact(wd, Contact(firstname="Arthur", middlename="Conan", lastname="Doyle", nikename="Sir", title="AD", company="Writers",
                address="Edinburgh Street", home="01215", mobile="03246", work="02458", fax="010",
                email="conan_arthur@gmail.com", email2="doyle@gmail.com", email3="acdoyle@gmail.com",
                homepage="www.doyle.com", bday="3", bmonth="May", byear="1839", aday="21", amonth="April", ayear="1930",
                address2="Wood Street 2", phone2="1", notes="B2"))
        self.return_to_homepage(wd)
        self.logout(wd)


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(contact.firstname)
    # fill in middlename
    wd.find_element_by_name("middlename").click()
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(contact.middlename)
    # fill in lastname
    wd.find_element_by_name("lastname").click()
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(contact.lastname)
    # fill in nikename
    wd.find_element_by_name("nickname").click()
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys(contact.nikename)
    # fill in title
    wd.find_element_by_name("title").click()
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys(contact.title)
    # fill in company
    wd.find_element_by_name("company").click()
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys(contact.company)
    # fill in address
    wd.find_element_by_name("address").click()
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys(contact.address)
    # fill in home
    wd.find_element_by_name("home").click()
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys(contact.home)
    # fill in mobile
    wd.find_element_by_name("mobile").click()
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(contact.mobile)
    # fill in work
    wd.find_element_by_name("work").click()
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys(contact.work)
    # fill in fax
    wd.find_element_by_name("fax").click()
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys(contact.fax)
    # fill in email
    wd.find_element_by_name("email").click()
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(contact.email)
    # fill in email2
    wd.find_element_by_name("email2").click()
    wd.find_element_by_name("email2").clear()
    wd.find_element_by_name("email2").send_keys(contact.email2)
    # fill in email3
    wd.find_element_by_name("email3").click()
    wd.find_element_by_name("email3").clear()
    wd.find_element_by_name("email3").send_keys(contact.email3)
    # fill in homepage
    wd.find_element_by_name("homepage").click()
    wd.find_element_by_name("homepage").clear()
    wd.find_element_by_name("homepage").send_keys(contact.homepage)
    # fill in bday
    wd.find_element_by_name("bday").click()
    wd.find_element_by_name("bday").send_keys(contact.bday)
    # fill in bmonth
    wd.find_element_by_name("bmonth").click()
    wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
    # fill in byear
    wd.find_element_by_name("byear").click()
    wd.find_element_by_name("byear").send_keys(contact.byear)
    # fill in aday
    wd.find_element_by_name("aday").click()
    wd.find_element_by_name("aday").send_keys(contact.aday)
    # fill in amonth
    wd.find_element_by_name("amonth").click()
    wd.find_element_by_name("amonth").send_keys(contact.amonth)
    # fill in ayear
    wd.find_element_by_name("ayear").click()
    wd.find_element_by_name("ayear").send_keys(contact.ayear)
    # fill in address2
    wd.find_element_by_name("address2").click()
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys(contact.address2)
    # fill in phone2
    wd.find_element_by_name("phone2").click()
    wd.find_element_by_name("phone2").clear()
    wd.find_element_by_name("phone2").send_keys(contact.phone2)
    # fill in notes
    wd.find_element_by_name("notes").click()
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys(contact.notes)