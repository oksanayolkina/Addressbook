def test_delete_group(app, init_login, create_if_not_groups, index, db):
    app.group.open_group_page()
    old_groups = db.get_group_list()
    app.group.delete_by_number(index)

    assert "Group has been removed" in app.message()

    app.group.return_to_group_page()

    # TODO: Deletion group in list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

    old_groups.pop(index)
    assert new_groups == old_groups
