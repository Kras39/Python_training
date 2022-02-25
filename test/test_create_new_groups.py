# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application



@pytest.fixture
def app(request):
    fixure = Application()
    request.addfinalizer(fixure.destroy)
    return fixure

def test_add_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", header="new_group", footer="new_group"))
    app.session.logout()

def test_add_empty_groups(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

