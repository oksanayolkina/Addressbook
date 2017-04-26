class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "{}".format(self.name)
