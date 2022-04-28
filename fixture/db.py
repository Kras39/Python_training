import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:


    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


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
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email,
                                    email2=email2, email3=email3, home=home, mobile=mobile, work=work, phone2=phone2))
        finally:
            cursor.close()
        return list


    def get_contact_list_without_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00' and id not in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home,
                            mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE deprecated ='0000-00-00 00:00:00' and `group_id` in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
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

    def get_group_id_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for group_id in cursor:
                (id,) = group_id
                list.append(str(id))
        finally:
            cursor.close()
        return list


    def get_groups_without_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list where group_id not in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list


    def remove_all_contacts_from_random_group(self, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from address_in_groups where group_id = {group_id}")
        finally:
            cursor.close()


    def remove_all_contacts_from_all_groups(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from address_in_groups")
        finally:
            cursor.close()


    def add_random_contact_to_random_group(self, contact_id, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO `address_in_groups` (`domain_id`, `id`, `group_id`, `created`, `modified`, `deprecated`) VALUES ('0', '{contact_id}', '{group_id}', '2022-04-10 00:00:00', '2022-04-10 00:00:00', '0000-00-00 00:00:00')")
        finally:
            cursor.close()


    def get_contact_id_in_group_list(self, contact_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select id from address_in_groups where id = {contact_id}")
            for row in cursor:
                (id) = row
                list.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()