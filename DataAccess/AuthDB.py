import json

from pymongo import MongoClient
from DataAccess.DB import get_database
#probably should make these static methods
# when u pass in string you should get the db collection
# not sure if it works if not use db_name['user']
# not sure if line 8 works if now just pass instring or dot notation
# ie client["users"] or client.users


@staticmethod
def storeCredentials(usr):
    try:
        if usr is not None:
            credentials = usr.GetCredentials()
            protectCollection = get_protector_db()
            result = protectCollection.insert_one(json.dumps(credentials))
            if not result.acknowledged:
                raise Exception('An error occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'Credentials stored successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'Credentials were not stored'
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def fetchCredentials(usrname):
    try:
        if usrname is None:
            raise ValueError('Username is required')
        else:
            protecCollection = get_protector_db()
            creds = protecCollection.find({'Username': usrname})
            if creds is None:
                res = {
                    'credentialsFound': False,
                    'message': 'User data not found'
                }
            else:
                res = {
                    'credentialsFound': True,
                    'message': 'User data found',
                    'credentials': creds
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def storeKeys(accountId, private_key, public_key):
    try:
        authInfo = {
            'AccountId': accountId,
            'PrivateKey': private_key.decode(),
            'PublicKey': public_key.decode()
        }
        authCollection = get_auths_db()
        result = authCollection.insert_one(json.dumps(authInfo))
        if not result.acknowledged:
            raise Exception('An error occurred while trying to connect to database')
        elif result.inserted_id is not None:
            data = {'success': True, 'message': 'User auth stored'}
        else:
            data = {'success': False, 'message': 'An error occurred while storing credentials'}
        return data
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def updatePublicKey(accountId, key):
    try:
        authCollection = get_auths_db()
        result = authCollection.update_one(
            {'AccountId': accountId},
            {"$set": {'publicKey': key}},
            upsert=True
        )
        # not sure if acknowledge is true if upsert fialed
        # was_success = result.acknowledge
        was_success = result.modified_count > 0
    except Exception as err:
        raise Exception(err) from err
    return was_success


@staticmethod
def fetchPublicKey(accountId):
    try:
        authCollection = get_auths_db()
        result = authCollection.find({'AccountId': accountId})
        if result is None:
            data = {
                'isInitial': True,
                'resultNotFound': True,
                'message': 'Account not found',
                'pubKey': None
            }
        else:
            data = {
                'isInitial': False,
                'resultNotFound': False,
                'message': None,
                'pubKey': result['publicKey']
            }
        return data
    except Exception as err:
        raise Exception(err) from err


def get_auths_db():
    db = get_database()
    return db.Auths


def get_protector_db():
    db = get_database()
    return db.Protectors
