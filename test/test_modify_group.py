from model.group import Group
from random import randrange

def test_modify_group(app, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_random_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
         app.group.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    old_groups = db.get_group_list()
    index=randrange(len(old_groups))
    group = json_groups
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)