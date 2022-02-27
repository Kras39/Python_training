from model.group import Group


def test_edit_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Portal Group", header="PG", footer="One of the nicest groups"))
    app.session.logout()