# count primes
# write a function called count_primes that takes an integer, N
# Return a number, the count of prime numbers that are found below the input number.
# Sieve of Eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def count_primes(N):
    count_of_prime_numbers = 0
    prime_numbers = []

    # check every number under N
    # if number is not devisible by one of the primes in the list
    # add to list, add to count

    for number in range(2,N):
        is_prime = True
        # if number in prime_numbers:
        #     found_primes.append(number)
        for prime in prime_numbers:
            if number % prime == 0:
                is_prime = False
                break    
        if is_prime:
            prime_numbers.append(number)
    print(prime_numbers)

    count_of_prime_numbers = len(prime_numbers)

    return count_of_prime_numbers

print(count_primes(18))
