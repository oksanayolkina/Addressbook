from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/a').click()
        # fill contact form
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Oks")
        wd.find_element_by_xpath("//div[@id='content']/form/input[2]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.middlename is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.middlename is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)

        # load foto
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").send_keys('C:\study\img\img-2.jpg')

        if contact.title is not None:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home)
        if contact.mobile is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile)
        if contact.work is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work)
        if contact.fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.fax)
        if contact.email is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2 is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage is not None:
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys("1986")
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys("2000")
        # wd.find_element_by_name("address2").click()
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[2]").click()
        if contact.address2 is not None:
            wd.find_element_by_name("address2").click()
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.address2)
        if contact.phone2 is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.phone2)
        if contact.notes is not None:
            wd.find_element_by_name("notes").click()
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit group form
        wd.find_element_by_name("submit").click()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        time.sleep(1)
        Alert(wd).accept()
        time.sleep(1)

    def delete_one_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[1]').click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        time.sleep(1)
        Alert(wd).accept()
        time.sleep(1)

    def is_contact_present(self):
        self.app.open_home_page()
        return self.app.is_element_present(By.NAME, "selected[]")

    def get_list(self):
        wd = self.app.wd
        self.open_group_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        groups = []
        for checkbox in checkboxes:
            name = checkbox.get_attribute("title")[8:-1]
            id = int(checkbox.get_attribute("value"))
            groups.append(Group(name=name, id=id))
        return groups

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        return len(checkboxes)