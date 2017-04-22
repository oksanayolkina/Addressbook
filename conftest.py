from web_api.addressbook_api import AddressBookAPI
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
