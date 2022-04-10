import random
from model.group import Group
from model.contact import Contact

def test_add_contact_in_group(app, db, data_contact, check_ui):
    contact = data_contact
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    app.contact.create_in_group(contact, group.name)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)

    if check_ui:
        contacts_in_ui_group = app.contact.get_contact_list_in_group(group.name)
        contacts_in_db_group = []
        for item in new_contacts:
            if item in contacts_in_ui_group:
                contacts_in_db_group.append(item)
        assert sorted(contacts_in_ui_group, key=Group.id_or_max) == sorted(contacts_in_db_group, key=Group.id_or_max)