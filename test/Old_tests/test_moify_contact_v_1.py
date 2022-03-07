from model.Old_model.contact_v_1 import Contact_v_1


def test_modify_firstname_contact(app):
    app.contact.modify_first_contact(Contact_v_1(firstname="Poppy"))

def test_modify_middlename_contact(app):
    app.contact.modify_first_contact(Contact_v_1(middlename="Jones"))

def test_modify_lastname_contact(app):
    app.contact.modify_first_contact(Contact_v_1(lastname="Patterson"))

def test_modify_nikename_contact(app):
    app.contact.modify_first_contact(Contact_v_1(nikename="GP"))

def test_modify_title_contact(app):
    app.contact.modify_first_contact(Contact_v_1(title="API"))

def test_modify_company_contact(app):
    app.contact.modify_first_contact(Contact_v_1(company="Prostor"))

def test_modify_address_contact(app):
    app.contact.modify_first_contact(Contact_v_1(address="36 Way"))

def test_modify_home_contact(app):
    app.contact.modify_first_contact(Contact_v_1(home="22-356"))

def test_modify_mobile_contact(app):
    app.contact.modify_first_contact(Contact_v_1(mobile="01-453-785"))

def test_modify_fax_contact(app):
    app.contact.modify_first_contact(Contact_v_1(fax="79-85-452"))

def test_modify_email_contact(app):
    app.contact.modify_first_contact(Contact_v_1(email="oster_oliver@navahoo.io"))

def test_modify_email2_contact(app):
    app.contact.modify_first_contact(Contact_v_1(email2="hotter-spot@yahoo.com"))

def test_modify_email3_contact(app):
    app.contact.modify_first_contact(Contact_v_1(email3="hotter42_spot@yahoo.com.io"))

def test_modify_homepage_contact(app):
    app.contact.modify_first_contact(Contact_v_1(homepage="www.33cow.com"))

def test_modify_bday_contact(app):
    app.contact.modify_first_contact(Contact_v_1(bday="13"))

def test_modify_bmonth_contact(app):
    app.contact.modify_first_contact(Contact_v_1(bmonth="May"))

def test_modify_byear_contact(app):
    app.contact.modify_first_contact(Contact_v_1(byear="1960"))

def test_modify_aday_contact(app):
    app.contact.modify_first_contact(Contact_v_1(aday="15"))

def test_modify_amonth_contact(app):
    app.contact.modify_first_contact(Contact_v_1(amonth="June"))

def test_modify_ayear_contact(app):
    app.contact.modify_first_contact(Contact_v_1(ayear="1983"))

def test_modify_address2_contact(app):
    app.contact.modify_first_contact(Contact_v_1(
        address2="Ius dicat feugiat no, vix cu modo dicat principes. Sea esse deserunt ei, no diam ubique euripidis has. An eos iusto solet, id mel dico habemus."))

def test_modify_phone2_contact(app):
    app.contact.modify_first_contact(Contact_v_1(phone2="33-489"))

def test_modify_notes_contact(app):
    app.contact.modify_first_contact(Contact_v_1(notes="F2"))

