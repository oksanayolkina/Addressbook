from db_api.addressbook_db import AddresbookDB
from db_api.addressbook_orm import AddressBookORM

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test"
}

# db = AddresbookDB(**config)
db = AddressBookORM(**config)

try:
        for c in db.get_group_list():
            print(c)
finally:
    pass
