from selenium import webdriver
from models.group import Group
import unittest

class test_cr_book(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        test_group = Group(name="gr_name", header="gr_header", footer="gr_footer")
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(test_group)
        self.return_to_group_page()
        self.logout()

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost:8888/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()

    def create_group(self, group):
        wd = self.wd
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group form
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self):
        wd = self.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
