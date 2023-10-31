import re

password = input("Input a stong password (mix of uppercase, lowercase, numbers, symbols) and at least 6 symbols: ")

if len(password) < 6:
    print("Minimum 6 symbols.")
elif re.search(r'[A-Z]', password) == None:
    print('At least one uppercase letter')
elif re.search(r'[a-z]', password) == None:
    print('At least one lowercase letter')
elif re.search(r'[0-9]', password) == None:
    print('At least one number')
elif re.search(r'[!@#$%^&*()_+=-]', password) == None:
    print('At least one symbol')
else:
    print(f"Congratulation. {password} is a strong password.")