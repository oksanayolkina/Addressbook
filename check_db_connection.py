from db_api.addressbook_orm import AddressBookORM
from models.group import Group

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test"
}

db = AddressBookORM(**config)

try:
    l = db.get_contacts_in_group(Group(id='171'))
    for c in l:
        print(c)
    print(len(l))
finally:
    pass
