# -*- coding: utf-8 -*-

from model.group import Group


def test_add_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", header="new_group", footer="new_group"))
    app.session.logout()

def test_add_empty_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

