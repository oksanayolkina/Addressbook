def test_add_group(app, init_login, test_group, db):
    app.group.open_group_page()
    old_groups = db.get_group_list()
    app.group.create(test_group)
    assert "A new group has been entered into the address book." in app.message()
    app.group.return_to_group_page()

    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups) - 1
    old_groups.append(test_group)
    assert sorted(old_groups) == sorted(new_groups)

