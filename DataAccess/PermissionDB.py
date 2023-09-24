from DataAccess.DB import get_database


@staticmethod
def fetchPermission(pid):
    try:
        if pid is None:
            raise ValueError('Permission id is required')
        else:
            permCollection = get_db()
            permission = permCollection.find_one({'Id': pid})
            if permission is None:
                res = {
                    'permissionExists': False,
                    'message': 'Permission not found'
                }
            else:
                res = {
                    'permissionExists': False,
                    'message': 'Permission found',
                    'permissionData': permission
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def fetchPermissionsByAccount(accountName):
    try:
        if accountName is None:
            raise ValueError('An account name is required')
        else:
            permCollection = get_db()
            permissions = permCollection.find({'Accounts.Name': accountName})
            if permissions is None:
                res = {
                    'permissionsExists': False,
                    'message': f'Permissions for {accountName} not found'
                }
            else:
                res = {
                    'permissionsExists': True,
                    'message': f'Permissions found for {accountName}',
                    'permissionsData': permissions
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def addPermission(permission):
    try:
        if permission is not None:
            permCollection = get_db()
            result = permCollection.insert_one(permission)
            if not result.acknoledged:
                raise Exception('A error occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'Permission added successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'Permission was not added'
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def updatePermissioin(permission):
    pass


def get_db():
    db = get_database()
    return db.Permissions
