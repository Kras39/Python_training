# -*- coding: utf-8 -*-

from model.edit_contact import EditFirstContact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.edit_contact.edit_first_contact(EditFirstContact(firstname="Richard", middlename="Grinch", lastname="Palmer", nikename="PG"))
    app.session.logout()
