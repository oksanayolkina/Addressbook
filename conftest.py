from web_api.addressbook_api import AddressBookAPI
from models.group import Group
from models.contact import Contact
import pytest

@pytest.fixture(scope="session")
def app():
    addr_app = AddressBookAPI()
    yield addr_app
    addr_app.destroy()

@pytest.fixture(scope="session")
def init_login(app):
    app.session.login(username="admin", password="secret")
    yield
    app.session.logout()

@pytest.fixture
def create_if_not_groups(app, init_login):
    if not app.is_group_present():
        test_group = Group(name="gr_name")
        app.create_group(test_group)

@pytest.fixture
def create_if_not_contacts(app, init_login):
    if not app.is_contact_present():
        test_contact = Contact(firstname="Oksana_name")
        app.create_contact(test_contact)