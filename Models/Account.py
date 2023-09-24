from Utils.Id_Geneerator import generateId


class Account:

    def __init__(self, id, name, admin, contact, orgs=None):
        self.Id = id
        self.Admin = admin
        self.Name = name
        self.Contact = contact
        self.Orgs = orgs

    def getAdmin(self):
        return self.Admin

    def getName(self):
        return self.Name

    def getContact(self):
        return self.Contact

    def getOrgs(self):
        return self.Orgs

    #might have to change synatx orgs are list of dicts
    def getOrg(self, orgId):
        return self.Orgs[orgId]

    def addOrg(self, org):
        self.Orgs.add(org)

    @classmethod
    def createNewAccount(cls, name, admin, contact, orgs=None):
        id = generateId()
        return cls(id, name, admin, contact, orgs)