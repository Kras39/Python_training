# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application



@pytest.fixture
def app(request):
    fixure = Application()
    request.addfinalizer(fixure.destroy)
    return fixure

def test_add_groups(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group", header="new_group", footer="new_group"))
    app.logout()

def test_add_empty_groups(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

