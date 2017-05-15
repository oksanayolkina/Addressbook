def test_delete_one_contact(app, init_login, create_if_not_contacts):
    app.open_home_page()
    app.contact.delete_one_contact()
    assert "Record successful deleted" in app.message()
