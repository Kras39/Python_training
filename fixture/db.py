import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,  home=home,
                                    mobile=mobile, work=work, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self, group_name):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select ad.id, ad.firstname, ad.lastname from addressbook ad, address_in_groups gr,group_list gl where"
            " ad.deprecated='0000-00-00 00:00:00' and ad.id = gr.id and gr.group_id = gl.group_id and gl.group_name=%s", [group_name])
            for a in cursor:
                (id, firstname, lastname) = a
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()