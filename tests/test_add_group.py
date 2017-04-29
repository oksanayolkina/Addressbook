from models.group import Group
import pytest

test_data = [
    Group(name="name", header="gr_header", footer="gr_footer"),
    # Group(name=None, header=None, footer=None),
    # Group(name=11, header=12, footer=13),
    # Group(name="gr_name", header="gr_header", footer="gr_footer")
    ]

@pytest.mark.parametrize("group", test_data, ids=[repr(b) for b in test_data])
def test_add_group(app, init_login, group):
    app.open_group_page()
    app.create_group(group)
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()

    # TODO: Verify group in grouplist
    assert "gr_name" or "name" in app.is_groups_present()

    # app.delete_group_by_number(0)
