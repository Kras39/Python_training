# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contacts import Contacts
from telephone import Telephone
from mailboxes_and_homepage import MailboxesAndHomepage
from birthday import Birthday
from secondary_address import SecondaryAddress


class AddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login_to_account(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, wd, contacts):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nikename)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)

    def create_telephone(self, wd, telephone):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(telephone.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(telephone.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(telephone.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(telephone.fax)

    def create_mailboxes_and_homepage(self, wd, mailboxes_and_homepage):
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(mailboxes_and_homepage.email)
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(mailboxes_and_homepage.email2)
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(mailboxes_and_homepage.email3)
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(mailboxes_and_homepage.homepage)

    def create_birthday(self, wd, birthday):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(birthday.bday)
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(birthday.bmonth)
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birthday.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(birthday.aday)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(birthday.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(birthday.ayear)

    def create_secondary_address(self, wd, secondary_address):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secondary_address.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(secondary_address.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(secondary_address.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_id("content").click()
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_to_account(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_new_contact(wd, Contacts(firstname="contact_1", middlename="contact_2", lastname="New Contact", nikename="NC", title="WP", company="New Company", address="Wood Street"))
        self.create_telephone(wd, Telephone(home="123", mobile="456", work="789", fax="010"))
        self.create_mailboxes_and_homepage(wd, MailboxesAndHomepage(email="contact_1@gmail.com", email2="contact_2@gmail.com", email3="contact_3@gmail.com", homepage="www.contact.com"))
        self.create_birthday(wd, Birthday(bday="1", bmonth="January", byear="1990", aday="1", amonth="January", ayear="2020"))
        self.create_secondary_address(wd, SecondaryAddress(address2="Wood Street 2", phone2="1", notes="B2"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_contacts_1(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login_to_account(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_new_contact(wd, Contacts(firstname="Peter", middlename="Climan", lastname="Nuck", nikename="NC", title="", company="", address="Wooding Road"))
        self.create_telephone(wd, Telephone(home="", mobile="456", work="", fax=""))
        self.create_mailboxes_and_homepage(wd, MailboxesAndHomepage(email="contact_1.2@gmail.com", email2="", email3="", homepage=""))
        self.create_birthday(wd, Birthday(bday="15", bmonth="January", byear="1993", aday="23", amonth="January", ayear="2000"))
        self.create_secondary_address(wd, SecondaryAddress(address2="Woody Street 2", phone2="14", notes="B2B"))
        self.return_to_home_page(wd)
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
