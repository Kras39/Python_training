# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contacts(app):
    app.contact.create(
        Contact(firstname="contact_1", middlename="contact_2", lastname="New Contact", nikename="NC", title="WP",
                company="New Company", address="Wood Street", home="123", mobile="456", work="789", fax="010",
                email="contact_1@gmail.com", email2="contact_2@gmail.com", email3="contact_3@gmail.com",
                homepage="www.contact.com", address2="Wood Street 2", phone2="1", notes="B2"))

def test_add_empty_contacts(app):
    app.contact.create(
        Contact(firstname="Arthur", middlename="Conan", lastname="Doyle", nikename="Sir", title="AD", company="Writers",
                address="Edinburgh Street", home="01215", mobile="03246", work="02458", fax="010",
                email="conan_arthur@gmail.com", email2="doyle@gmail.com", email3="acdoyle@gmail.com",
                homepage="www.doyle.com", address2="Wood Street 2", phone2="1", notes="B2"))


