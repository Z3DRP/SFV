from DataAccess.DB import get_database


@staticmethod
def fetchGroup(groupId):
    try:
        if groupId is None:
            raise ValueError('Group id is requried')
        else:
            groupCollection = get_db()
            group = groupCollection.find_one({'GroupId': groupId})
            if group is None:
                res = {
                    'groupExists': False,
                    'message': 'Group not found'
                }
            else:
                res = {
                    'groupExists': True,
                    'message': 'Group found',
                    'groupData': group
                }
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def addGroup(group):
    try:
        if group is None:
            raise ValueError('Group data is required')
        else:
            groupCollection = get_db()
            result = groupCollection.insert_one(group)
            if not result.acknoledged:
                raise Exception('A issue occurred while connecting to database')
            elif result.inserted_id is not None:
                res = {
                    'success': True,
                    'message': 'Group has been added successfully'
                }
            else:
                res = {
                    'success': False,
                    'message': 'Group was not added'
                }
    except Exception as err:
        raise Exception(err) from err


@staticmethod
def updateGroup(group):
    try:
        groupCollection = get_db()
        result = groupCollection.update_one(
            {'groupId': group.GroupId},
            {'$set': {
                'Accounts': group.Accounts,
                'Name': group.Name,
                'NumberOfMembers': group.NumberOfMembers,
                'Users': group.Users
            }},
            upsert=True
        )
        wasSuccess = result.modified_count > 0
        if wasSuccess:
            res = {
                'success': wasSuccess,
                'result': result,
                'message': 'Group was successfully updated'
            }
        else:
            res = {
                'success': wasSuccess,
                'result': None,
                'message': 'Group was not updated'
            }
    except Exception as err:
        raise Exception(err) from err


def get_db():
    db = get_database()
    return db.Groups

