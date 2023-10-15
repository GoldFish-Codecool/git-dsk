from datetime import datetime
current_date = datetime.now()
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
next_birthday = datetime(current_date.year, birthdate.month, birthdate.day)
if current_date > next_birthday:
    next_birthday = datetime(current_date.year + 1, birthdate.month, birthdate.day)
days_until_next_birthday = (next_birthday - current_date).days
print(f"Days until your next birthday: {days_until_next_birthday} days")
