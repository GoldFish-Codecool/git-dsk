#Create a program that finds all prime numbers up to a given number

def prime (n):
  for i in range (2, n):
    if n % i == 0:
      return False
  return True
n = int(input("please input a number: "))
for i in range (2,n):
  if prime (i):
    print (i)
