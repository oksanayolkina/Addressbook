from models.contact import Contact
import pytest

test_data = [
    Contact(firstname="Oksana", middlename="Olegovna", lastname="Yolkina", nickname="oksana", title="QA",
            company="Company", address="Ukraine, Kyiv", home="+38(044)111-22-33", mobile="+38(044)111-22-33",
            work="+38(044)111-22-33", fax="+38(044)111-22-33", email="oksana.yolkina@gmail.com",
            email2="oksana.yolkina2@gmail.com", email3="oksana.yolkina3@gmail.com", homepage="http://vk.com",
            address2="Ukraine, Nikopol", phone2="+38(056)123-45-67", notes="other information"),
    Contact(firstname="Test")
    ]

@pytest.mark.parametrize("contact", test_data, ids=[repr(b) for b in test_data])
def test_add_contact(app, init_login, contact):
    app.create_contact(contact)
    assert "Information entered into address book." in app.message()
    app.open_home_page()

    # TODO: Verify contact in contactlist

    # app.delete_all_contacts()