"""
Find the first number whose square is > 1000
"""
for n in range(1, 40):
    n_squared = n ** 2
    if n_squared > 1000:
        print(n, n_squared)
