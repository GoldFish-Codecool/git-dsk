def is_palindrome(input_string):
    clean_string = input_string.replace(" ", "").lower()
        return clean_string == clean_string[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
