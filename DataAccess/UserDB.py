import json

from DataAccess.DB import get_database


@staticmethod
def fetchUserId(usrname):
    try:
        if usrname is None:
            raise ValueError('Username is required')
        else:
            usrCollection = get_db()
            usr = usrCollection.find_one({'username': usrname})
            if usr is None:
                res = {
                    'userExists': False,
                    'message': 'User was not found'
                }
            else:
                res = {
                    'userExists': True,
                    'message': 'User found',
                    'userId': usr['userId']
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def fetchUser(usrname):
    try:
        if usrname is None:
            raise ValueError('Username is required')
        else:
            usrCollection = get_db()
            usr = usrCollection.find_one({'username': usrname})
            if usr is None:
                res = {
                    'userExists': False,
                    'message': 'User not found'
                }
            else:
                return {
                    'userExists': True,
                    'message': 'User found',
                    'userData': usr
                }
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def addUser(usr):
    try:
        if usr is not None:
            usrInfo = usr.GetUserData()
            usrCollection = get_db()
            result = usrCollection.insert_one(json.dumps(usrInfo))
            if not result.acknowledged:
                raise Exception('A error occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'User was added successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'User was not added'
                }
    except Exception as err:
        raise Exception(err) from err


def get_db():
    db = get_database()
    return db.Users

