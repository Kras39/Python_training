import random
from model.group import Group
from model.contact import Contact

def test_add_some_contact_in_some_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Quechua'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Allure"))
    if len(db.get_contact_list_without_groups()) == 0:
        app.contact.create(Contact(firstname="Allure"))
    all_groups = db.get_group_list()
    group_for_add = (random.choice(all_groups)).id
    contacts_in_group_before = orm.get_contacts_in_group(Group(id=group_for_add))
    contact_not_in_group = random.choice(orm.get_contacts_not_in_group(Group(id=group_for_add)))
    app.contact.add_contact_to_some_group(contact_not_in_group.id, group_for_add)
    contacts_in_group_after = orm.get_contacts_in_group(Group(id=group_for_add))
    assert (len(contacts_in_group_after) == len(contacts_in_group_before) + 1)
    contacts_in_group_before.append(contact_not_in_group)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after,
                                                                             key=Contact.id_or_max)


def test_delete_contact_from_some_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Quechua'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Allure"))
    all_groups = db.get_group_list()
    group_for_adding = (random.choice(all_groups)).id
    contact_not_in_group = random.choice(orm.get_contacts_not_in_group(Group(id=group_for_adding)))
    if len(db.get_group_list_with_contacts()) == 0:
        app.contact.add_contact_to_group_via_grid_by_id(contact_not_in_group.id, group_for_adding)
    group_list_with_contacts = db.get_group_list_with_contacts()
    group_for_remove_contact = (random.choice(group_list_with_contacts)).id
    contacts_in_group_before = orm.get_contacts_in_group(Group(id=group_for_remove_contact))
    contact_id_to_delete_from_group = random.choice(contacts_in_group_before)
    app.contact.delete_contact_from_some_group(contact_id_to_delete_from_group.id, group_for_remove_contact)
    contacts_in_group_after = orm.get_contacts_in_group(Group(id=group_for_remove_contact))
    assert (len(contacts_in_group_before) - 1 == len(contacts_in_group_after))
    contacts_in_group_before.remove(contact_id_to_delete_from_group)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after,
                                                                             key=Contact.id_or_max)