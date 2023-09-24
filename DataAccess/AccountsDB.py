from DataAccess.DB import get_database


@staticmethod
def fetchAccount(accountName):
    try:
        if accountName is None:
            raise ValueError('Account name is required')
        else:
            accountCollection = get_db()
            account = accountCollection.find({'Name': accountName})
            if account is None:
                res = {
                    'accountExists': False,
                    'message': 'Account not found'
                }
            else:
                res = {
                    'accountExists': True,
                    'message': 'Account found',
                    'accountData': account
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def addAccount(account):
    try:
        if account is not None:
            accountCollection = get_db()
            result = accountCollection.insert_one(account)
            if not result.acknowledged:
                raise Exception('A error occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'Account was added successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'Account was not added'
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def updateAccount(account):
    pass


def get_db():
    db = get_database()
    return db.Accounts
