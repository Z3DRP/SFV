import os

@staticmethod
def getSalt():
    return 'SaltyBananaTaco'

@staticmethod
def get_secret(cls):
    return os.urandom(64)