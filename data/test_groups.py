import string, random, json, os.path
from models.group import Group

utf_symbols = ''.join([chr(l) for l in range(1, 0x10ffff) if chr(l).isprintable()])
cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF) if chr(l).isprintable()])
cyr_symbol_ru_uk = ''.join([chr(l) for l in range(0x0410, 0x0457) if chr(l).isprintable()])


def random_string(maxlen):
    length = random.randrange(maxlen)
    symbols = string.ascii_letters + string.digits + " "*10 + cyr_symbol_ru_uk #+ string.punctuation
    return ''.join([random.choice(symbols) for _ in range(length)])


# names = ['', 'hgvjhsdfcs', "123"]
# headers = ['', 'hgvjhsdfcs', "123"]
# footers = ['', 'hgvjhsdfcs', "123"]
#
# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in names
#     for header in headers
#     for footer in footers
# ] + [
#     Group(name=random_string(14), header=random_string(20), footer=random_string(50))
#     for _ in range(5)
# ]

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "group_data.json")

# test_groups = []
with open(file_name, encoding="utf-8") as f:
    test_data = [Group(**data) for data in json.load(f)]
    # for data in json.load(f):
    #     test_groups.append(Group(**data))

test_data += [
    Group(name=random_string(14), header=random_string(20), footer=random_string(50))
    for _ in range(5)
]