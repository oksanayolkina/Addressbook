def test_modife_group(app, init_login, create_if_not_groups):
    app.open_group_page()
    app.modife_group_by_number(0)
    assert "Group record has been updated." in app.message()
    app.return_to_group_page()
