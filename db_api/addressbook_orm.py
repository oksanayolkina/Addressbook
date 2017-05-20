from pony.orm import *
from pymysql.converters import conversions
from datetime import datetime
from models.group import Group
from models.contact import Contact

class AddressBookORM:

    db = Database()

    class GroupORM(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set("ContactORM", table="address_in_groups", column="id", reverse="groups", lazy=True)

        def get_model(self):
            return Group(id=self.id, name=self.name, header=self.header, footer=self.footer)

    class ContactORM(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        middlename = Optional(str, column="middlename")
        nickname = Optional(str, column="nickname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set("GroupORM", table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

        def get_model(self):
            return Contact(id=self.id, firstname=self.firstname, lastname=self.lastname, middlename=self.middlename, nickname=self.nickname)

    def __init__(self, host, port, user, password, db):
        self.db.bind("mysql", host=host, port=port, user=user, password=password, db=db, charset="utf8",
                     conv=conversions)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list(self):
        query = select(g for g in self.GroupORM).order_by(self.GroupORM.name, self.GroupORM.id)
        return [g.get_model() for g in query]

    @db_session
    def get_contact_list(self):
        query = select(c for c in self.ContactORM if c.deprecated is None)
        return [c.get_model() for c in query]

    @db_session
    def get_contacts_in_group(self, group):
        dbgroup = select(g for g in self.GroupORM if g.id == group.id).first()
        return [c.get_model() for c in dbgroup.contacts]

