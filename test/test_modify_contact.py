from model.contact import Contact
from random import randrange

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Poppy", middlename="Conan", lastname="Doyle", nikename="Mr", title="PCD", company="Writers",
                address="Edinburgh Street 33", home="71215", mobile="93246", work="32458", fax="010",
                email="conan_dolly@gmail.com", email2="doyle@gmail.com", email3="pcdoyle@gmail.com",
                homepage="www.poopy_doyle.com", address2="Nord Wood Street 2", phone2="33-22-568", notes="GG")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Snoop", middlename="Dog", lastname="Doyle", nikename="Mr", title="PCD", company="Singers",
                address="Edinburgh Street 44", home="70000", mobile="90000", work="30000", fax="0004",
                email="snoop_dolly@gmail.com", email2="dog_snoop@gmail.com", email3="mrdogy@gmail.com",
                homepage="www.snoopy_dog.com", address2="Nord Wood Street 88", phone2="33-44-568", notes="SG")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_random_contact(app, json_contact):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contact
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)