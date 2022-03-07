# -*- coding: utf-8 -*-

from model.Old_model.contact_v_1 import Contact_v_1


def test_add_contacts(app):
    app.contact.create(
        Contact_v_1(firstname="contact_1", middlename="contact_2", lastname="New Contact", nikename="NC", title="WP",
                company="New Company", address="Wood Street", home="123", mobile="456", work="789", fax="010",
                email="contact_1@gmail.com", email2="contact_2@gmail.com", email3="contact_3@gmail.com",
                homepage="www.contactic.com", bday="1", bmonth="January", byear="1990", aday="1", amonth="January",
                ayear="2020", address2="Wood Street 2", phone2="1", notes="B2"))

def test_add_empty_contacts(app):
    app.contact.create(
        Contact_v_1(firstname="Arthur", middlename="Conan", lastname="Doyle", nikename="Sir", title="AD",
                    company="Writers", address="Edinburgh Street", home="01215", mobile="03246", work="02458", fax="010",
                email="conan_arthur@gmail.com", email2="doyle@gmail.com", email3="acdoyle@gmail.com",
                homepage="www.doyle.com", bday="3", bmonth="May", byear="1839", aday="21", amonth="April", ayear="1930",
                address2="Wood Street 2", phone2="1", notes="B2"))