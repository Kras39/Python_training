import re
from random import randrange
from model.contact import Contact

# Трансформация тестов для проверки информации о контактах на главной странице. Реализация сравнения для всех записей,
# а не для одной случайно выбранной. Сравнение с информацией, загруженной из базы данных.

def test_all_contact_info_on_the_home_page(app, db):
    contacts_list_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_list_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_list_ui) == len(contacts_list_db)
    for i in range(0, len(contacts_list_db)):
        contact_from_home_page = contacts_list_ui[i]
        contact_list_db = contacts_list_db[i]
        assert contact_from_home_page.id == contact_list_db.id
        assert contact_from_home_page.firstname == contact_list_db.firstname
        assert contact_from_home_page.lastname == contact_list_db.lastname
        assert contact_from_home_page.address == contact_list_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_list_db)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_list_db)

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