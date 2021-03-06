def test_add_group(app, init_login, test_group, db):
    app.group.open_group_page()
    old_groups_list = db.get_group_list()
    app.group.create(test_group)
    assert "A new group has been entered into the address book." in app.message()
    app.group.return_to_group_page()

    new_groups_list = db.get_group_list()
    assert len(old_groups_list) == len(new_groups_list) - 1
    old_groups_list.append(test_group)
    assert sorted(old_groups_list) == sorted(new_groups_list)

