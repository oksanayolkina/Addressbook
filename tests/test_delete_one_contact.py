def test_delete_one_contact(app, init_login):
    app.open_home_page()
    app.delete_one_contact()
    assert "Record successful deleted" in app.message()
