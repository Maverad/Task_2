import string
import random

class GenerateTestData:

    def generate_random_email(self, length:int=5):
        if length == 0 or length > 10:
             length = 5
        email = ''
        letters = string.ascii_letters
        chars = []
        domens = ['@ya.ru', '@google.com', '@rambler.com']
        for i in range(length):
            chars.append(letters[random.randint(0, 51)])
            email = ''.join(chars)
        return email + random.choice(domens)

    def generate_random_name(self, length:int=5):
        if length == 0 or length > 10:
            length = 5
        name = ''
        letters = string.ascii_letters
        chars = []
        for i in range(length):
            chars.append(letters[random.randint(0, 51)])
            name = ''.join(chars)
        return name

    def generate_random_password(self, length:int=5):
        if length == 0 or length > 10:
            length = 5
        password = ''
        letters = string.ascii_letters
        digits = string.digits
        chars = []
        for i in range(length):
            chars.append(random.choice(letters))
            chars.append(random.choice(digits))
            password = ''.join(chars)
        return password 

