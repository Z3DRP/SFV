import unittest
from Models.User import User
from Utils.Authenticator import Authenticator as auth
from Utils.SFV_Protector import SFV_Protector as protector

class TestEncryption(unittest.TestCase):
    def setup(self):
        # create user and plain text password
        self.tito = User.createUser('titoBrown', 'titoman1@gmail.con', False)
        self.tito.setPlainTxtPassword('z3d_D3v')
        # setup data for encryption
        self.publicKey, self.privateKey = protector.getKeys()
        self.data = 'This represents a org attribute that will be encrypted and stored in db'

    def test_encryptPassword(self):
        hashedPwd = auth.getHash(self.tito.Password)
        self.assertTrue(hashedPwd != 'z3d_D3v', 'Hashed password is equal to original password')

    def test_verifyPassword(self):
        hashedPwd = auth.getHash(self.tito.Password)
        isValidPwd = auth.compareHash(self.tito.Password, hashedPwd)
        self.assertTrue(isValidPwd, 'Hashed passwords expected to match but did not')

    def test_encryptOrgData(self):
        encryptedData = protector.encrypt(self.data, self.publicKey)
        self.assertTrue(self.data != encryptedData, 'Original data matched encrypted data')

    def test_decryptOrgData(self):
        decryptedData = protector.encrypt(self.data, self.privateKey)
        self.asserEqual(self.data, decryptedData, 'Decrypted data did not match orginal data')        


if __name__ == '__main__':
    unittest.main()