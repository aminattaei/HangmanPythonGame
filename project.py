from abc import ABC,abstractmethod
import random
from time import sleep

class PasswordManager(ABC):

    @abstractmethod
    def generate(self):
        pass


class PasswordStrGenerator(PasswordManager):
    def generate(self): # type: ignore
        
        letters = 'abcdefghijklmnopqrstuvwxyz'

        random_str = ''

        for _ in range(20):
            random_str += random.choice(letters)

        return random_str


class PasswordNumberGenerator(PasswordManager):
    def generate(self): # type: ignore
        random_str = ''
        random_numbers = range(1,100)
        for _ in range(0,10):
            random_str += str(random.choice(random_numbers))

        return random_str

class PasswordStrongGenerator(PasswordStrGenerator,PasswordNumberGenerator):
    
    def generate(self): # type: ignore
        return super().generate() + PasswordNumberGenerator.generate(self)



class PasswordStrongCharGenerator(PasswordStrGenerator,PasswordNumberGenerator):
    def generate(self): # type: ignore
        random_str = ''
        chars = '!@#$%^&*()?></'
        for _ in range(20):
            random_str += random.choice(chars)

        return super().generate()[0:20] + random_str[0:20] + super().generate()[20:]  + PasswordNumberGenerator.generate(self) + random_str[21:]


while True:
    new_pass = PasswordStrongCharGenerator()
    print(new_pass.generate())
    print("-" * 90)
    sleep(1)