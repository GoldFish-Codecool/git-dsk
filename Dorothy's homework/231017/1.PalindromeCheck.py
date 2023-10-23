def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    clean_string = input_string.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return clean_string == clean_string[::-1]

# Input string to check for a palindrome
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
