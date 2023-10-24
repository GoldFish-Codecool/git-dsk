#Password Validator: Design a tool that checks if a given password meets certain criteria: a mix of uppercase, lowercase, numbers, symbols, and a minimum length. The program should provide feedback on which criteria the password fails.


def is_valid_password(password):
  criteria_met = True
  if len(password) < 8:
      print("Password too short - min 8 characters.")
      criteria_met = False

  has_uppercase = any(char.isupper() for char in password)
  if not has_uppercase:
      print("Uppercase letter missing.")
      criteria_met = False

  has_lowercase = any(char.islower() for char in password)
  if not has_lowercase:
      print("Lowercase letter missing.")
      criteria_met = False

  has_digit = any(char.isdigit() for char in password)
  if not has_digit:
      print("Number missing.")
      criteria_met = False

  has_symbol = any(char in "!@#$%^&*()-_+=<>?/[]{}|\\:;" for char in password)
  if not has_symbol:
      print("Symbol missing.")
      criteria_met = False

  return criteria_met

def main():
  password = input("Enter your password: ")
  if is_valid_password(password):
      print("\nCongratulations! Your password is ok.")
  else:
      print("\nPassword not strong enough - fix the identified errors.")

if __name__ == "__main__":
  main()
