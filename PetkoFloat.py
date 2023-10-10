n = int(input("How many numbers do you want to compare? "))
largest = float('-inf')
for i in range(n):
    num = float(input("Enter number " + str(i+1) + " (negative and decimals allowed): "))
    if num > largest:
        largest = num
print("The largest number among the entered numbers is:", largest)
