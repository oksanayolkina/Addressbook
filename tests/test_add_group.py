from models.group import Group

def test_add_group(app):
    test_group = Group(name="gr_name", header="gr_header", footer="gr_footer")
    app.open_group_page()
    app.create_group(test_group)
    # TODO: Verify message for group creation
    app.return_to_group_page()
    # TODO: Verify group in grouplist