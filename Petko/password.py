import random
import string

def generate_password(passlength):
    if passlength < 8:
        return "Password length should be at least 8 characters"
    else:
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numeric = string.digits
        symbols = string.punctuation
        all = lowercase + uppercase + numeric + symbols

        temp = random.sample(all,length)

        password = "".join(temp)

        return password

length = int(input("Enter the number of characters for the password (minimum of 8 characters): "))
print(f"Your new password is: {generate_password(length)}")
