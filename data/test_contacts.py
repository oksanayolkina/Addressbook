import string, random, json, os.path
from models.contact import Contact

utf_symbols = ''.join([chr(l) for l in range(1, 0x10ffff) if chr(l).isprintable()])
cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF) if chr(l).isprintable()])
cyr_symbol_ru_uk = ''.join([chr(l) for l in range(0x0410, 0x0457) if chr(l).isprintable()])


def random_string(maxlen):
    length = random.randrange(maxlen)
    symbols = string.ascii_letters + string.digits + " "*10 + cyr_symbol_ru_uk #+ string.punctuation
    return ''.join([random.choice(symbols) for _ in range(length)])


# firstnames = ['', 'hgvjhsdfcs', "123"]
# middlenames = ['', 'hgvjhsdfcs', "123"]
# lastnames = ['', 'hgvjhsdfcs', "123"]
# nickname = ['', 'hgvjhsdfcs', "123"]

#
# test_data = [
#     Contact(name=name, header=header, footer=footer, nickname=nickname)
#     for firstname in firstnames
#     for middlename in middlenames
#     for lastname in lastnames
#     for nickname in nicknames

# ] + [
#     Group(firstname=random_string(14), middlename=random_string(20), lastname=random_string(50), nickname=random_string(50))
#     for _ in range(5)
# ]

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contact_data.json")

# test_groups = []
with open(file_name, encoding="utf-8") as f:
    test_data_c = [Contact(**data) for data in json.load(f)]
    # for data in json.load(f):
    #     test_groups.append(Group(**data))

test_data_c += [
    Contact(firstname=random_string(14), middlename=random_string(20), lastname=random_string(50), nickname=random_string(50))
    for _ in range(5)
]


# for example (название полей)
# Contact(firstname="Oksana", middlename="Olegovna", lastname="Yolkina", nickname="oksana", title="QA",
#             company="Company", address="Ukraine, Kyiv", home="+38(044)111-22-33", mobile="+38(044)111-22-33",
#             work="+38(044)111-22-33", fax="+38(044)111-22-33", email="oksana.yolkina@gmail.com",
#             email2="oksana.yolkina2@gmail.com", email3="oksana.yolkina3@gmail.com", homepage="http://vk.com",
#             address2="Ukraine, Nikopol", phone2="+38(056)123-45-67", notes="other information")