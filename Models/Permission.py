from Utils.Id_Geneerator import generateId


class Permission:

    def __init__(self, id, usr, read, write, accountId, modifyAll):
        self.Id = id
        self.UserId = usr
        self.Read = read
        self.Write = write
        self.AccountId = accountId
        self.ModifyAll = modifyAll

    def CanWrite(self):
        return self.Write

    def CanRead(self):
        return self.Read

    def GetAccountId(self):
        return self.AccountId

    def GetUser(self):
        return self.User

    @classmethod
    def CreateNewPermission(cls, usr, read, write, accountId):
        id = generateId()
        modifyAll = read and write
        return cls(id, usr, read, write, accountId, modifyAll)