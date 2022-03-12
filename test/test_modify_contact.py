from model.contact import Contact

def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Poppy", middlename="Conan", lastname="Doyle", nikename="Mr", title="PCD", company="Writers",
                address="Edinburgh Street 33", home="71215", mobile="93246", work="32458", fax="010",
                email="conan_dolly@gmail.com", email2="doyle@gmail.com", email3="pcdoyle@gmail.com",
                homepage="www.poopy_doyle.com", address2="Nord Wood Street 2", phone2="33-22-568", notes="GG")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)