from DataAccess import PermissionDB, GroupsDB
from Models.User import User
from Models.AdminGroup import AdminGroup
from Models.Permission import Permission as perm

class AdminUser(User):

    def __init__(self, accounts=None, users=None, groups=None):
        self.Accounts = accounts
        self.Users = users
        self.Groups = groups

    def assignPermission(self, usr, canRead, canWrite, account):
        permission = perm.CreateNewPermission(usr.Id, canRead, canWrite, account.Id)
        # database saved needs to be moved out into controller for now just create obj
        # result = PermissionDB.addPermission(permission)
        usr.HasWritePermissions = canWrite
        usr.HasReadPermissions = canRead
        if canWrite:
            usr.WriteableAccounts.append(account)
        if canRead:
            usr.ReadableAccounts.append(account)

        res = {
            'success': True,
            'message': 'Permission has been assigned',
            'permission': permission
        }
        # if result.get('success'):
        #     res = {
        #         'success': True,
        #         'message': 'Permission has bee assigned',
        #         'permission': permission
        #     }
        # else:
        #     res = {
        #         'success': False,
        #         'message': 'An error occurred while assigning permission'
        #     }
        return res
    
    def updatePermission(self, permission, usr, canRead, canWrite, account):
        permission.Read = canRead
        permission.Write = canWrite
        permission.ModifyAll = canRead and canWrite
        usr.HasWritePermissions = canWrite
        usr.HasReadPermissions = canRead    
        if canWrite and account not in usr.WriteableAccounts:
            usr.WriteableAccounts.append(account)
        if canRead and account not in usr.ReadableAccounts:
            usr.ReadableAccounts.append(account)
        if not canWrite and account in usr.WriteableAccounts:
            usr.WriteableAccounts.remove(account)
        if not canRead and account in usr.ReadableAccounts:
            usr.ReadableAccounts.remove(account)

        res = {
            'success': True,
            'message': 'Permission has been updated',
            'permission': permission
        }
        return res


    def createAdminGroup(self, groupName, users, accounts):
        group = AdminGroup.CreateNewGroup(groupName, users, accounts)
        result = GroupsDB.addGroup(group)

        if result.get('success'):
            res = {
                'success': True,
                'message': 'Admin Group has been created'
            }
        else:
            res = {
                'success': False,
                'message': 'An error occurred while creating Admin Group'
            }
        return res
    
    def assignUserGroup(self, user, groupId):
        group = GroupsDB.fetchGroup(groupId)
        group['users'].add(user)
        result = GroupsDB.updateGroup(group)

        if result.get('success'):
            res = {
                'success': True,
                'message': 'User has been assigned to group successfully'
            }
        else:
            res = {
                'success': False,
                'message': 'An error occurred while assigning user to group'
            }
        return res

    def getAdminGroups(self):
        return self.Groups

    def addAccount(self, name, contact, contractLength, details):
        pass

    def getUserId(self, username):
        pass

    def getGroupId(self, name):
        pass

    def moveUser(self, usrId, groupId):
        pass

    def removeUser(self, userId):
        pass

    def getAccountOrgs(self, accountId):
        pass

    def getUserData(self):
        data = User.getUserData(self)
        data['Accounts'] = self.Accounts
        data['Users'] = self.Users
        data['Groups'] = self.Groups
        return data
