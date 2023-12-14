even_squares = (
    x ** 2
    for x in range(50_000_000)
    if x % 2 == 0
)

print('Squares is a', even_squares)

for even_square in even_squares:
    if even_square > 100:
        break
    print(even_square)
