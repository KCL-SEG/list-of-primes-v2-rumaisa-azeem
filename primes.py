"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be greater than 0")
    list = []
    counter = 1
    num_primes_found = 0
    while num_primes_found < number_of_primes:
        counter += 1
        half_counter = counter//2
        is_prime = True
        for j in range(2, half_counter+1):
            if counter%j == 0: # divisible by something so move on
                is_prime = False
                break
        if is_prime:
            list.append(counter)
            num_primes_found += 1
        
    return list


primes(10)