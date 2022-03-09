from model.contact import Contact

def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="Poppy"))

def test_modify_middlename_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename=""))
    app.contact.modify_first_contact(Contact(middlename="Jones"))

def test_modify_lastname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.modify_first_contact(Contact(lastname="Archi"))

def test_modify_nikename_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nikename=""))
    app.contact.modify_first_contact(Contact(nikename="GP"))

def test_modify_title_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title=""))
    app.contact.modify_first_contact(Contact(title="API"))

def test_modify_company_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(company=""))
    app.contact.modify_first_contact(Contact(company="Prostor"))

def test_modify_address_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address=""))
    app.contact.modify_first_contact(Contact(address="36 Way"))

def test_modify_home_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home=""))
    app.contact.modify_first_contact(Contact(home="22-356"))

def test_modify_mobile_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(mobile=""))
    app.contact.modify_first_contact(Contact(mobile="01-453-785"))

def test_modify_fax_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fax=""))
    app.contact.modify_first_contact(Contact(fax="79-85-452"))

def test_modify_email_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email=""))
    app.contact.modify_first_contact(Contact(email="oster_oliver@navahoo.io"))

def test_modify_email2_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email2=""))
    app.contact.modify_first_contact(Contact(email2="hotter-spot@yahoo.com"))

def test_modify_email3_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email3=""))
    app.contact.modify_first_contact(Contact(email3="hotter42_spot@yahoo.com.io"))

def test_modify_homepage_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(homepage=""))
    app.contact.modify_first_contact(Contact(homepage="www.33cow.com"))

def test_modify_address2_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address2=""))
    app.contact.modify_first_contact(Contact(address2="Ius dicat feugiat no, vix cu modo dicat principes. Sea esse deserunt ei, no diam ubique euripidis has. An eos iusto solet, id mel dico habemus."))

def test_modify_phone2_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(phone2="-"))
    app.contact.modify_first_contact(Contact(phone2="33-489"))

def test_modify_notes_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(notes="-"))
    app.contact.modify_first_contact(Contact(notes="F2"))