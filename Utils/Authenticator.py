import hashlib

from Utils.Secrets import getSalt
from DataAccess import UserDB
from Utils.SFV_Auth import SFV_Auth


# derived form abstract class need to overide encrypt decrypt
class Authenticator(SFV_Auth):
            
    @staticmethod
    def compareHash(plainTxt, encryptdPwd):
        plainTxt += getSalt()
        newHash = Authenticator.getHash(plainTxt)
        return newHash == encryptdPwd


    @staticmethod
    def getHash(plainTxt):
        plainTxt += getSalt()
        return hashlib.sha512(plainTxt.encode('utf-8')).hexdigest()

