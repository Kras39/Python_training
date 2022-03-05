from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Super_new_group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new_header"))

def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="new_footer"))
