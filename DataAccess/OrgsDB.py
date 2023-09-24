from DataAccess.DB import get_database


@staticmethod
def fetchOrgByEnv(accountName, environment):
    try:
        if environment is None or accountName is None:
            raise ValueError('Org id and environment are required')
        else:
            orgCollection = get_db()
            org = orgCollection.find({
                "$and": [
                    {'AccountName': {"$eq": accountName}},
                    {'Environment': {"$eq": environment}}
                ]
            })
            if org is None:
                res = {
                    'orgExists': False,
                    'message': f'{environment} environment was not found for {accountName}'
                }
            else:
                res = {
                    'orgExists': True,
                    'message': f'{environment} environment found for {accountName}'
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def addOrg(org):
    try:
        if org is not None:
            orgCollection = get_db()
            result = orgCollection.insert_one(org)
            if not result.acknowledged:
                raise Exception('An error occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'Org has been added successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'Org was not added'
                }
            return res
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def updateOrg(org):
    try:
        if org is None:
            raise ValueError('Org is required')
        orgCollection = get_db()
        result = orgCollection.update_one(
            {'Id': org.Id},
            {"$set": {
                'AccountName': org.AccountName,
                'Name': org.Name,
                'Environment': org.Environment,
                'LoginURL': org.LoginURL,
                'Username': org.Username,
                'Password': org.Password,
                'CustomFields': org.CustomFields
            }},
            upsert=True
        )
        wasSuccess = result.modified_count > 0
        if wasSuccess:
            res = {
                'success': True,
                'message': 'Org was updated successfully'
            }
        else:
            res = {
                'success': False,
                'message': 'Org was not updated'
            }
        return res
    except Exception as err:
        raise Exception(err) from err


def get_db():
    db = get_database()
    return db.Orgs