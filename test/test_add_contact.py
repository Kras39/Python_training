from model.contact import Contact

def test_add_contact(app, data_contact):
    contact = data_contact
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # time.sleep (6)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    # time.sleep(6)
    o = sorted(old_contacts, key=Contact.id_or_max)
    n = sorted(new_contacts, key=Contact.id_or_max)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app, json_contact):
    contact = json_contact
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1  == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    o = sorted(old_contacts,key=Contact.id_or_max)
    n = sorted(new_contacts,key=Contact.id_or_max)
    assert sorted(old_contacts,key=Contact.id_or_max)  ==  sorted(new_contacts,key=Contact.id_or_max)