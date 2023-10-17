def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    prime_list = []
    for number in range(start, end + 1):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers = find_primes_in_range(start, end)
print("Prime numbers in the range {} to {} are: {}".format(start, end, prime_numbers))
