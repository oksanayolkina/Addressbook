import pytest
from models.group import Group

def test_delete_group(app, init_login, create_if_not_groups):
    app.open_group_page()
    app.delete_group_by_number(0)
    assert "Group has been removed" in app.message()
    app.return_to_group_page()
    # TODO: Deletion group in list

