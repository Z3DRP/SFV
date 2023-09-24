import unittest
from Models.StandardUser import StandardUser as StdUsr
from Models.AdminUser import AdminUser as AdmUsr
from Models.Account import Account
from Models.Org import Org
from Models.AdminGroup import AdminGroup as group

class TestPermissions(unittest.TestCase):

    def setUp(self):
        self.stdUsr = StdUsr(id = None,username='titoBrown', email='tbrowny2@gmail.com', isAdmin=False)
        self.adminUsr = AdmUsr.createUser('zedDev', 'z3d3v1@gmail.com', isAdmin=True) # AdmUser does not have a createUser method. Use the User class instead here.
        self.account = Account.createNewAccount('Alpha1Omega', self.adminUsr, 'Boberto Holmes')
        usrs = [self.stdUsr]
        self.group = group.createNewGroup('Admin1', usrs, self.account)
        self.stdUsr.Groups.append(self.group)
        self.org = Org.createNewOrg(
            self.account,
            'Alpha1Dev',
            'Development',
            'https://alphaOne@my.salesforce.alphadev.com',
            'sfdc-zd3v-support@gmail.com',
            self.account
        )

    def test_assignPermission(self):
        result = AdmUsr.assignPermission(
            user = self.stdUsr, 
            canWrite = True,
            canRead = True,
            account = self.account
        )
        permission = result['permission']
        self.assertEquals(permission.UserId, self.stdUsr.Id, 'Permission was not assigned to the correct user')
        self.assertEquals(permission.Read, True, 'Read permission expected to be true')
        self.assertEquals(permission.Write, True, 'Write permissions expected to be true')
        self.assertEquals(permission.AccountId, self.account.Id, 'Permission account id did not match')
        self.assertEquals(permission.ModifyAll, True, 'Modify all expected to be true')
        self.assertEquals(self.stdUsr.HasWritePermissions, True, 'std user expected to have write permissions')
        self.assertEquals(self.stdUsr.HasReadPermissions, True, 'std user expected to have read permissions')
        self.assertEquals(len(self.stdUsr.WriteableAccounts), 1, 'std usr writeable accounts expected to contain 1')
        self.assertEquals(len(self.stdUsr.ReadableAccounts), 1, 'std usr readable accounts expected to contain 1')

    def test_updatePermission(self):
        result = AdmUsr.assignPermission(
            user = self.stdUsr,
            canRead = True,
            canWrite = True,
            account = self.account
        )
        updatedResult = AdmUsr.updatePermission(
            permission = result['permission'],
            user = self.stdUsr,
            canRead = False,
            canWrite = False,
            account = self.account
        )
        updatedPermision = updatedResult['permission']
        self.assertEquals(updatedPermision.UserId, self.stdUsr.Id, 'User id of permission changed when it should not')
        self.assertEquals(updatedPermision.Read, False, 'Read permission expected to update to false and did not')
        self.assertEquals(updatedPermision.Write, False, 'Write permission expected to update to false but did not')
        self.assertEquals(updatedPermision.AccountId, self.account.Id, 'Permission account id did not match')
        self.assertEquals(updatedPermision.ModifyAll, False, 'Modify all permission expected to be false')
        self.assertEquals(self.stdUsr.HasWritePermissions, False, 'std usr expected to not have write permissions')
        self.assertEquals(self.stdUsr.HasReadPermissions, False, 'std usr expect to not have read permissions')
        self.assertEquals(len(self.stdUsr.ReadableAccounts), 0, 'std user expected to have no readable accounts')
        self.assertEqual(len(self.stdUsr.WriteableAccounts), 0, 'std usr expected to not have any writeable accounts')


if __name__ == '__main__':
    unittest.main()