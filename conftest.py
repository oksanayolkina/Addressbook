import pytest, random, json, os.path
from web_api.addressbook_api import AddressBookAPI
from models.group import Group
from models.contact import Contact
from data.test_groups import test_data
from db_api.addressbook_orm import AddressBookORM

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--config", action="store", default="config.json")

@pytest.fixture(scope="session")
def config(request):
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config"))
    with open(file_name) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def app(request, config):
    browser = request.config.getoption("--browser")
    addr_app = AddressBookAPI(browser=browser, base_url=config["web"]["base_url"])
    yield addr_app
    addr_app.destroy()

@pytest.fixture(scope="session")
def db(config):
    dbfixture = AddressBookORM(**config["db"])
    yield dbfixture
    # dbfixture.destroy()

@pytest.fixture(scope="session")
def init_login(app, config):
    app.session.login(username=config["web"]["username"], password=config["web"]["password"])
    yield
    app.session.logout()

@pytest.fixture
def create_if_not_groups(app, init_login):
    if not app.group.is_group_present():
        test_group = Group(name="gr_name")
        app.group.create(test_group)

@pytest.fixture
def create_if_not_contacts(app, init_login):
    if not app.is_contact_present():
        test_contact = Contact(firstname="Oksana_name")
        app.create_contact(test_contact)

@pytest.fixture(params=[0, "random", -1], ids=["first", "random", "last"])
def index(app, request):
    if request.param == "random":
        return random.randrange(1, app.group.count())
    return request.param

@pytest.fixture(params=test_data, ids=[repr(b) for b in test_data])
def test_group(request):
    return request.param
