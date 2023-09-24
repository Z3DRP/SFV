from Models.User import User


class StandardUser(User):

    def __init__(self, id, username, email, isAdmin=False, pwd=None,  permissions=None, readAccounts=None, writeAccounts=None):
        self.Permissions = permissions
        self.ReadableAccounts = readAccounts
        self.WriteableAccounts = writeAccounts
        self.HasWritePermissions = self.ReadableAccounts.length > 0
        self.HasReadPermissions = self.WriteableAccounts.length > 0
        self.Groups = None
        User.__init__(self, id, username, email, isAdmin, pwd)

    def getAllPermissions(self):
        return self.Permissions

    def hasWrite(self):
        return self.HasWritePermissions

    def hasRead(self):
        return self.HasReadPermissions

    def getPermission(self, permissionId):
        return self.Permissions[permissionId]

    def getGroups(self):
        return self.Groups

    def getGroup(self, groupId):
        return self.Groups[groupId]

    def getNumberOfAccounts(self):
        return self.WriteableAccounts.length + self.ReadableAccounts.length

    def getUserData(self):
        data = User.getUserData(self)
        data['Permissions'] = self.Permissions
        data['ReadableAccounts'] = self.ReadableAccounts
        data['WriteableAccounts'] = self.WriteableAccounts
        data['HasWritePermissions'] = self.HasWritePermissions
        data['HasReadPermissions'] = self.HasReadPermissions
        data['Groups'] = self.Groups
        return data
    
