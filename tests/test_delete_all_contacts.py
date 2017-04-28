def test_delete_all_contacts(app, init_login, create_if_not_contacts):
    app.open_home_page()
    app.delete_all_contacts()

    assert "Record successful deleted" in app.message()
