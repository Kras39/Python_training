from model.contact import Contact
from random import randrange

def test_add_first_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.add_first_contact_to_group()