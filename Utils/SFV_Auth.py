#needs to be abstract class
from abc import ABC, abstractmethod
class SFV_Auth:

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
