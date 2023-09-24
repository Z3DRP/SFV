import unittest
from Tests import test_Encryption, test_Permissions

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_Encryption.TestEncryption))
    test_suite.addTest(unittest.makeSuite(test_Permissions.TestPermissions))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())