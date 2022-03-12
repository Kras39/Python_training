# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contacts(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Arthur", middlename="Conan", lastname="Doyle", nikename="Sir", title="AD", company="Writers",
                address="Edinburgh Street", home="01215", mobile="03246", work="02458", fax="010",
                email="conan_arthur@gmail.com", email2="doyle@gmail.com", email3="acdoyle@gmail.com",
                homepage="www.doyle.com", address2="Wood Street 2", phone2="1", notes="B2")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

