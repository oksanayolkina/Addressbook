from web_api.addressbook_api import AddressBookAPI
import pytest

@pytest.fixture()
def app():
    app = AddressBookAPI()
    app.login(username="admin", password="secret")
    yield app
    app.logout()
    app.destroy()