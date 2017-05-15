def test_modify_group(app, init_login, create_if_not_groups, test_group, index):
    data_to_modify = test_group
    app.group.open_group_page()
    old_groups = app.group.get_list()
    app.group.modife_by_number(index, data_to_modify)
    assert "Group record has been updated." in app.message()
    app.group.return_to_group_page()

    new_groups = app.group.get_list()

    if data_to_modify.name is not None:
        old_groups[index].name = data_to_modify.name

    assert len(old_groups) == len(new_groups)
    assert new_groups == old_groups

