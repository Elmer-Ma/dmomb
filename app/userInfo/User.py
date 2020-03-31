class User:
    def __init__(self, u_id, name, number, mail, password, createAt, updateAt):
        self.u_id = u_id
        self.name = name
        self.number = number
        self.mail = mail
        self.password = password
        self.createAt = createAt
        self.updateAt = updateAt

    @property
    def u_id(self):
        return self.u_id

    @u_id.setter
    def u_id(self, u_id):
        self.u_id = u_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, number):
        self.number = number

    @property
    def mail(self):
        return self.mail

    @mail.setter
    def mail(self, mail):
        self.mail = mail
        @property
    def createAt(self):
        return self.createAt

    @createAt.setter
    def createAt(self, createAt):
        self.createAt = createAt

    @property
    def updatedAt(self):
        return self.updatedAt

    @updatedAt.setter
    def updatedAt(self, updatedAt):
        self.updatedAt = updatedAt
