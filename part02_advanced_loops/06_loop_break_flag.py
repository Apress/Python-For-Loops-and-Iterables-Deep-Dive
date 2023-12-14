"""
All prime numbers between 1000 and 1100
"""

for n in range(1000, 1100):

    # Is n not a prime number,
    # i.e. can it be divided by a smaller whole number
    is_prime = True
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            # Not a prime, break out of the inner loop
            is_prime = False
            break

    if is_prime:
        print(n)
