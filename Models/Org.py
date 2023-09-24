from Utils.Id_Geneerator import generateId
from Utils.Authenticator import Authenticator as auth

class Org:

    def __init__(self, id, account, name, env, url, usrname, pwd, customFields=None):
        self.Id = id
        self.AccountName = account
        self.Name = name
        self.Environment = env
        self.LoginURL = url
        self.Username = usrname
        self.Password = auth.getHash(pwd)
        self.CustomFields = customFields

    def getName(self):
        return self.Name

    def getEnvironment(self):
        return self.Environment

    def getCredentials(self):
        return [self.Username, self.Password]

    def getCustomFields(self):
        return self.CustomFields

    @classmethod
    def createNewOrg(cls, account, name, env, url, usrname, pwd, customFields):
        id = generateId()
        return cls(id, account, name, env, url, usrname, pwd, customFields)
