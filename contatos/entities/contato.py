class Contato:
    def __init__(self, id, createdate, email, firstname, hs_object_id, lastmodifieddate, lastname):
        self.id = id
        self.createdate = createdate
        self.email = email
        self.firstname = firstname
        self.hs_object_id = hs_object_id
        self.lastmodifieddate = lastmodifieddate
        self.lastname = lastname

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def createdate(self):
        return self.__createdate

    @createdate.setter
    def createdate(self, createdate):
        self.__createdate = createdate

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @property
    def hs_object_id(self):
        return self.__hs_object_id

    @hs_object_id.setter
    def hs_object_id(self, hs_object_id):
        self.__hs_object_id = hs_object_id

    @property
    def lastmodifieddate(self):
        return self.__lastmodifieddate

    @lastmodifieddate.setter
    def lastmodifieddate(self, lastmodifieddate):
        self.__lastmodifieddate = lastmodifieddate

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname
