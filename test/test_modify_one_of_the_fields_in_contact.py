from model.contact import Contact

def test_modify_firstname_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Poppy"))

def test_modify_lastname_contact(app):
    app.contact.modify_first_contact(Contact(lastname="Archi"))

def test_modify_company_contact(app):
    app.contact.modify_first_contact(Contact(company="Prostor"))


# def test_modify_bday_contact(app):
    # app.session.login(username="admin", password="secret")
    # app.contact.modify_first_contact(Contact(bday="24"))
    # app.session.logout()