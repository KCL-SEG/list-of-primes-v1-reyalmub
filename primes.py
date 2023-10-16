"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for number in range(len(number_of_primes)):
        if number % 2 ==1:
            list.append(number)
        
    return list
