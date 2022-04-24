import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

dbORM = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

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


def test_added_cont_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    if len(db.get_contact_list_without_groups()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    groups = db.get_group_list()
    for group in groups:
        app.contact.select_group_by_id_for_add_contact(group.id)
        app.contact.del_all_contacts_in_group()
        app.open_home_page()
    group_for_adding = random.choice(db.get_group_list()).id
    contacts_in_group_before = dbORM.get_contacts_in_group(Group(id=group_for_adding))
    contact_not_in_group = random.choice(dbORM.get_contacts_not_in_group(Group(id=group_for_adding)))
    app.contact.add_contact_in_group(contact_not_in_group.id, group_for_adding)
    contacts_in_group_after = dbORM.get_contacts_in_group(Group(id=group_for_adding))
    assert len(contacts_in_group_after) == len(contacts_in_group_before) + 1
    contacts_in_group_before.append(contact_not_in_group)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after, key=Contact.id_or_max)