"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    number = 1
    while len(list) < number_of_primes:
        if isPrime(number):
            list.append(number)
        number+=1
    return list
