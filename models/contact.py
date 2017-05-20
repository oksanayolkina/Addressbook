class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.id = id
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __repr__(self):
        return "id: {}, firstname: {}, middlename: {}, lastname: {}, nickname: {}".format(self.id, self.firstname, self.middlename, self.lastname, self.nickname)

    # сравнение на равенство
    def __eq__(self, other):
        if self.id is None or other.id is None:
            return self.id == other.id
        else:
            return self.id == other.id #and self.firstname == other.firstname

    # сортировка
    def __lt__(self, other):
        if self.id is None:
            return False
        elif other.id is None:
            return True
        else:
            return self.id < other.id
