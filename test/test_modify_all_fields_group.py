from model.group import Group


def test_modify_all_fields_in_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Portal Group", header="PG", footer="One of the nicest groups"))
    app.session.logout()