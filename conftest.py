from web_api.addressbook_api import AddressBookAPI
from models.group import Group
import pytest

@pytest.fixture(scope="session")
def app():
    app = AddressBookAPI()
    yield app
    app.destroy()

@pytest.fixture(scope="session")
def init_login(app):
    app.login(username="admin", password="secret")
    yield
    app.logout()

@pytest.fixture
def create_if_not_groups(app, init_login):
    if not app.is_group_present():
        test_group = Group(name="gr_name")
        app.create_group(test_group)
