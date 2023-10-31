import re


def is_valid_password(password):
  feedback = []

  if not re.search(r"[a-z]", password):
    feedback.append("Password must contain at least one lowercase letter")
  if not re.search(r"[A-Z]", password):
    feedback.append("Password must contain at least one uppercase letter")
  if not re.search(r"[0-9]", password):
    feedback.append("Password must contain at least one digit")
  if not re.search(r"[@#$%^&*()]", password):
    feedback.append("Password must contain at least one symbol")
  if len(password) < 8:
    feedback.append("Password must be at least 8 characters long")
  if not feedback:
    return "Valid password"
  else:
    return "/n".join(feedback)


while True:
  password = input("Enter a password: ")
  result = is_valid_password(password)
  if result == "Valid password":
    print("Password is valid.")
    break
  else:
    print("Invalid password. PLease try again.")

