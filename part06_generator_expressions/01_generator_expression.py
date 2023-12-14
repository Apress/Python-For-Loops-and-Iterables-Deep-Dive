squares = (
    x ** 2
    for x in range(50_000_000)
)

print(f'Squares is a\n{squares}\n')

for square in squares:
    if square > 10:
        break
    print(square)
