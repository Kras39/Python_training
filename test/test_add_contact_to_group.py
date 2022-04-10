from random import *
import random
from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name='test'))
        groups = db.get_group_list()
        if len(check_free_contact(groups, db)) == 0:
            app.contact.create(Contact(firstname='test'))
        free_contacts = check_free_contact(groups, db)
        free_contact_in_group = free_contacts[0]
        group_id = free_contact_in_group[1]
        free_contacts = free_contact_in_group[0]
        free_contact = free_contacts[0]
        app.contact.add_contact_to_group(free_contact.id, group_id)
        contacts_in_group = db.get_contacts_in_group(Group(id=group_id))[0]
        list_of_id = []
        for item in contacts_in_group:
            list_of_id.append(item.id)
        assert free_contact.id in list_of_id

def check_free_contact(groups, db):
    free_contacts = []
    for i in range(0, len(groups)):
        group = groups[i]
        if db.get_contacts_not_in_group(group)[0] != []:
            free_contacts.append(db.get_contacts_not_in_group(group))
    return free_contacts


    # contacts = db.get_contact_list()
    # contact = choice(contacts)
    # group_number = randrange(len(db.get_group_list()))
    # app.contact.add_contact_to_group(contact.id, group_number)
