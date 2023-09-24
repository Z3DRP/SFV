from Utils.Id_Geneerator import generateId


class AdminGroup:

    def __init(self, id, accounts, name, users, numberOfMembers=None):
        self.Id = id
        self.Accounts = accounts
        self.Name = name
        self.NumberOfMembers = numberOfMembers
        self.Users = users

    def getAccount(self, accountId):
        return self.Accounts[accountId]

    def getAccounts(self):
        return self.Accounts

    def getName(self):
        return self.Name

    def getUsers(self):
        return self.Users

    def getUser(self, uid):
        return self.Users[uid]

    @classmethod
    def createNewGroup(cls, name, users, accounts=None):
        aid = generateId()
        return cls(aid, accounts, name, users, len(users))