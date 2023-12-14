all_squares = (
    number ** 2
    for number in range(10)
)

even_squares = (
    number
    for number in all_squares
    if number % 2 == 0
)

print(', '.join(str(square) for square in even_squares))

# Longer version, with added line breaks
# print(
#     ', '.join(
#         str(square) for square in even_squares
#     )
# )

# No need to do this
# print(', '.join (( str(square) for square in even_squares )) )
