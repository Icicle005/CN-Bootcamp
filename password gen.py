import string
import random
 
pwd = input('Input Characters for your password: ')
length = len(pwd)
def generate_password(length):
    password = ''
    for char in range(length):
        rand = random.choice(pwd)
        password = password + rand
    return password
 
print('Your random password: ',generate_password(length))