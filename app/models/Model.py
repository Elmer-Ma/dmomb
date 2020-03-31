class Model:
    def __init__(self, m_id, u_id, d_id, name, paper, file_path, info, createAt):
        self.m_id = m_id
        self.u_id = u_id
        self.d_id = d_id
        self.name = name
        self.paper = paper
        self.file_path = file_path
        self.info = info
        self.createAt = createAt
        self.updatedAt = updatedAt

    @property
    def m_id(self):
        return self.m_id

    @m_id.setter
    def m_id(self, m_id):
        self.m_id = m_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def paper(self):
        return self.paper

    @paper.setter
    def paper(self, paper):
        self.paper = paper

    @property
    def file_path(self):
        return self.file_path

    @file_path.setter
    def file_path(self, file_path):
        self.file_path = file_path

    @property
    def info(self):
        return self.info

    @info.setter
    def info(self, info):
        self.info = info

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
