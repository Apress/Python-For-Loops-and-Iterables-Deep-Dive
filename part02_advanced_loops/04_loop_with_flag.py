"""
Find the first number whose square is > 1000
"""
found = False
for n in range(1, 40):
    n_squared = n ** 2
    if n_squared > 1000 and not found:
        print(n, n_squared)
        found = True
