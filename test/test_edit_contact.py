# -*- coding: utf-8 -*-

from model.edit_contact import EditContact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.edit_contact.edit(EditContact(firstname="Richard", middlename="Grinch", lastname="Palmer", nikename="PG"))
    app.session.logout()
