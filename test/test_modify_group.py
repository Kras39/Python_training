from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_test"))
    app.group.modify_first_group(Group(name="Super_new_group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="name_test"))
    app.group.modify_first_group(Group(header="new_header"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="name_test"))
    app.group.modify_first_group(Group(footer="new_footer"))

