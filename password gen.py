import string
import random
 
pwd_char = input('Input Characters for your password: ')
length = len(pwd_char)
def pwd(length):
    password = ''
    for i in range(length):
        rand = random.choice(pwd_char)
        password = password + rand
    return password
 
print('Your random password: ',pwd(length))