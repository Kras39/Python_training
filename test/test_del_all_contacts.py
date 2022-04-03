from model.contact import Contact
from random import randrange

def test_delete_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_all_contacts(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index:index-1] = []
    assert old_contacts == new_contacts
