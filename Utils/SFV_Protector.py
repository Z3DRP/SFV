import rsa as rsa

from Utils.Secrets import getSalt
from DataAccess import AuthDB
from Utils.SFV_Auth import SFV_Auth


class SFV_Protector(SFV_Auth):

    def __init__(self):
        self.__salt = 'saltyBurrito'
        self.__PubKey = None
        self.__PrivKey = None
        self.EncryptedData = None
        self.PlainTxt = None

    # @staticmethod
    # def Encrypt(plainTxt, privateKey):
    #     #self.__PubKey = SFV_Protector.fetchPublicKey(accountId)
    #     if privateKey is not '':
    #         plainTxt += getSalt()
    #         pwd = rsa.encrypt(plainTxt.encode(), privateKey)
    #     else:
    #         pwd = None
    #     return pwd
    
    @staticmethod
    def encrypt(plainTxt, pubKey):
        plaintTxt += getSalt()
        return rsa.encrypt(plainTxt.encode(), pubKey) if pubKey != '' else None

    # def Decrypt(self, hashData, accountId):
    #     # will have to remove salt
    #     self.__PubKey = SFV_Protector.fetchPublicKey(accountId)
    #     if self.__PubKey is not '':
    #         self.PlainTxt = rsa.decrypt(hashData, self.__PubKey).decode()
    #         self.PlainTxt = self.PlainTxt[:len(self.PlainTxt) - self.__salt]
    #     else:
    #         self.PlainTxt = None
    @staticmethod
    def decrypt(encryptedTxt, privKey):
        try:
            if encryptedTxt == '':
                raise ValueError('Encrypted data must be supplied')
            else:
                decryptedData = rsa.decrypt(encryptedTxt, privKey)
                return decryptedData[:len(decryptedData - getSalt())] 
        except Exception as err:
            raise Exception(err) from err

    @staticmethod
    def fetchPublicKey(self, account):
        try:
            publickey = AuthDB.fetchPublicKey(account)
            if publickey['resultNotFound'] is not True:
                key = publickey['publicKey']
            else:
                key = ''
            return key
        except Exception as err:
            raise Exception(err)

        
    @staticmethod
    def getKeys(self):
        try:
            public, private = rsa.newkeys(512)
        except Exception as err:
            raise err
        return [public, private]