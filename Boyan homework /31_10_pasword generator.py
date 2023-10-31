import random
import string

l = int(input("How many letters do you want the pasword to have?"))


def generate_password(length=l):

    characters = string.ascii_letters + string.digits + '?' + '.' + '!'
    password = ''.join(random.choice(characters) for i in range(length))
    return password


password = generate_password()
print ("generated password:", password)
