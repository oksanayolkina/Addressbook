def test_add_contact(app, init_login, test_contact, db):
    app.open_home_page()
    old_list_contacts = db.get_contact_list()
    app.contact.create_contact(test_contact)
    assert "Information entered into address book." in app.message()
    app.open_home_page()
    new_list_contacts = db.get_contact_list()
    assert len(old_list_contacts) == len(new_list_contacts) - 1
    old_list_contacts.append(test_contact)
    assert sorted(old_list_contacts) == sorted(new_list_contacts)
