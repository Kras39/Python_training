import random
from model.group import Group
from model.contact import Contact

def test_add_some_contact_in_some_group(app, db, orm):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_in_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)

def test_delete_some_contact_from_some_group(app, db, orm):
    app.group.create_group_if_it_not_exist(Group(name="test"))
    app.contact.create_contact_if_it_not_exist(Contact(firstname="test"))
    groups = db.get_group_id_with_contacts()
    if groups == []:
        contacts_list = db.get_contact_list()
        groups_list = db.get_group_list()
        some_contact = random.choice(contacts_list)
        some_group = random.choice(groups_list)
        app.contact.add_contact_in_group(some_contact.id, some_group.id)
        groups = db.get_group_id_with_contacts()
    group_id = random.choice(groups)
    contacts = orm.get_contacts_in_group(Group(id=group_id))
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(contact.id, group_id)
    assert contact in orm.get_contacts_not_in_group(Group(id=group_id))