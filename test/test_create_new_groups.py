from model.group import Group


def test_add_groups(app):
    app.group.create(Group(name="new_group", header="new_group", footer="new_group"))

def test_add_empty_groups(app):
    app.group.create(Group(name="", header="", footer=""))


