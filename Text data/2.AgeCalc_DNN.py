from datetime import datetime
current_date=datetime.now()
birthday=input("Please, enter your birth date in the following format (YYYY-MM-DD): ")
# Convert the input string to a datetime object
birthdate_date = datetime.strptime(birthday, "%Y-%m-%d")
# Calculate the age
age = current_date.year - birthdate_date.year - ((current_date.month, current_date.day) < (birthdate_date.month, birthdate_date.day))
# Print the age
print(f"You are {age} years old.")