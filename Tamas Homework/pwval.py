# 9. **Password Validator**:
#  - Design a tool that checks if a given password meets certain criteria: a mix of uppercase, lowercase, numbers, symbols, and a minimum length. The program should provide feedback on which criteria the password fails.

def contains_uppercase(password):
  for char in password:
    if char.isupper():
        return True
  return False

def contains_lowercase(password):
  for char in password:
    if char.islower():
      return True
  return False

def contains_number(password):
  for char in password:
    if char.isdigit():
      return True
  return False

def contains_symbol(password):
  for char in password:
    if char in "§+!%/=()":
      return True
  return False

if __name__=="__main__":
  password = input ("Input password: ")

  if len(password) < 8:
    print("Password is too short.")

  elif len(password) > 16:
    print("Password is too long.")
  
  elif not contains_uppercase(password):
    print("Password does not contain uppercase")

  elif not contains_lowercase(password):
    print("Password does not contain lowercase")

  elif not contains_number(password):
    print("Password does not contain number")

  elif not contains_symbol(password):
    print("Password does not contain symbol: §+!%/=()")

  else:
    print("Password is valid.")