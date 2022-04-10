import re
from random import randrange
from model.contact import Contact

# Проверка информации по некоторому (случайному) контакту из списка

def test_all_contact_info_on_the_home_page(app, json_contact):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

# Проверка информации по полю "All phones" для первого контакта из списка

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# Проверка соответствия информации по первому из списка контакту на странице "Details" и главной странице

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

# Трансформация тестов для проверки информации о контактах на главной странице. Реализация сравнения для всех записей,
# а не для одной случайно выбранной. Сравнение с информацией, загруженной из базы данных.

# def test_date_on_home_page(app, db):
    # if db.get_contact_list() == 0:
        # app.contact.create(Contact(firstname="TEST"))
    # old_contacts = db.get_contact_list()
    # randrange(len(old_contacts))
    # contact_from_home_page = app.contact.get_contact_list()
    # assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

# Выполняем очистку лишних символов с помощью применения регулярных выражений

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

def test_all_data_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(contacts_from_home_page)):
        contact_from_home_page = contacts_from_home_page[index]
        contact_from_db = contacts_from_db[index]
        assert contact_from_home_page.firstname == contact_from_db.firstname.strip()
        assert contact_from_home_page.lastname == contact_from_db.lastname.strip()
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)