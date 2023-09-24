from DataAccess import UserDB
from Utils.Id_Geneerator import generateId
from Utils.Authenticator import Authenticator as auth

class User:

    def __init__(self, usrId, usrname, emailAddress, isAdminUsr, pwd=None):
        self.Uid = usrId
        self.Username = usrname
        self.Email = emailAddress
        self.IsAdmin = isAdminUsr
        self.Password = pwd

    def getUsername(self):
        return self.username

    def isAdminProfile(self):
        return self.isAdmin

    def getEmail(self):
        return self.email

    def setPassword(self, pwdHash):
        self.Password = pwdHash

    def setPlaintTxtPassword(self, plainTxtPwd):
        self.Password = plainTxtPwd

    def getUserData(self):
        return {
            'Uid': self.Uid,
            'Username': self.Username,
            'Email': self.Email,
            'IsAdmin': self.IsAdmin
        }

    def getUserCredentials(self):
        return {
            'Uid': self.Uid,
            'Username': self.Username,
            'Password': self.Password
        }

    @classmethod
    def setNewUser(cls, usrname, email, plainTxtPwd):
        userId = generateId()
        hashedPwd = auth.getHash(plainTxtPwd)
        return cls(usrId=userId, usrname=usrname, emailAddress=email, pwd=hashedPwd)
    
    def createUser(self, username, email, isAdmin):
        self.Uid = generateId()
        self.Username = username
        self.Email = email
        self.IsAdmin = isAdmin

    @classmethod
    def setUserLogin(cls, username, password):
        return cls(None, usrname=username, emailAddress=None, pwd=password)

    @staticmethod
    def verify_user(self):
        try:
            usr = UserDB.fetchUser(self.Username)
            if not usr.get('userExists'):
                self.isValidUser = False
                raise ValueError(usr.get('message'))
            else:
                isValidPwd = auth.compareHash(self.PlainTextPassword, usr['usserData']['Password'])
                #newHash = Authenticator.getHash(self.PlainTextPassword)
                if isValidPwd:
                    userData = {
                        'isMatch': True,
                        'userId': usr['userData']['userId'],
                        'password': usr['userData']['password'],
                        'email': usr['userData']['email']
                    }
                else:
                    userData = {
                        'isMatch': False,
                        'message': 'Invalid password, check password and try again'
                    }

                return userData

        except Exception as err:
            raise Exception(err) from err

